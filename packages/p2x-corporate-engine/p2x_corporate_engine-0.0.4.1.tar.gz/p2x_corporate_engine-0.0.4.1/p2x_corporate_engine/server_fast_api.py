import asyncio
import json
import logging
from p2x_corporate_engine.engine import Engine
import yaml
from fastapi import FastAPI, Request
from p2x_corporate_engine.language_mapping import LANGUAGE_MAPPING

logger = logging.getLogger("p2x_server")
logger.setLevel(logging.INFO)


class ApiServer:

    def __init__(self, config: str = None, serialized: bool = False):
        self.app = FastAPI()
        self.config = config

        @self.app.on_event("startup")
        async def startup():
            self.app.state.lock = asyncio.Lock()

            if serialized:
                if os.environ.get("PYTHONTRANSLATIONSERVERDEBUG", None) is not None:
                    dbug = True
                else:
                    dbug = False
                Engine.setup_log(dbug=dbug)
                with open("engine.pkl", "rb") as engine_bts:
                    self.app.state.engine = pickle.load(engine_bts)
            else:
                with open(self.config, "r") as file:
                    config = yaml.safe_load(file)
                self.app.state.engine = Engine(config)

        @self.app.get("/healthcheck")
        async def healthcheck():
            return "ok"

        @self.app.post("/isready")
        async def handle_ready():
            return {"rc": 0}

        @self.app.post("/translate")
        async def handle_translate(request: Request):
            lock = self.app.state.lock
            engine = self.state.engine

            try:
                req = await request.json()
                batch = None
                src_lc = req.get("src")
                tgt_lc = req.get("tgt")
                batch = req.get("srcs")
                logging.info((LANGUAGE_MAPPING[src_lc]))
                logging.info((LANGUAGE_MAPPING[tgt_lc]))

                translations = None
                translations = await engine.process_batch(batch, LANGUAGE_MAPPING[src_lc], LANGUAGE_MAPPING[tgt_lc], lock)
                ans = {
                    "tus": []
                }
                for src, translation in zip(batch, translations):
                    ans["tus"].append({"src": src, "tgt": translation})
                return ans

            except Exception as e:
                logging.exception("ERROR in handle_translate: " + str(e))
                logging.info("BATCH: " + str(batch))
                logging.info("TRANSLATIONS: " + str(translations))
                logging.info("REQ: " + str(req))
                response_obj = {'status': 'failed', 'reason': str(e)}
                return response_obj
