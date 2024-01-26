# from pangeamt_nlp.translation_model.translation_model_factory import (
#    TranslationModelFactory,
# )
import logging
from pangeamt_nlp.seg import Seg
from p2x_corporate_engine.pipeline import Pipeline
from typing import Dict, List
from asyncio import Lock
import os
import json
import ctranslate2
import sentencepiece as spm

NO_LONELY_TRANSLATABLE_CHARS = "\n\t/n/t \u200b"


class Engine:
    def __init__(self, config: Dict, log_file: str = None, dbug: bool = False):
        self.setup_log(log_file, dbug)
        self._config = config
        self._gpu = self._config["translation_engine_server"]["gpu"]
        self._model = self.load_model()
        self._pipeline = Pipeline(self._config)

    def load_model(self):
        name = self._config["translation_engine_server"]["name"]
        model_path = self._config["translation_engine_server"]["model"]
        tokenizer_path = self._config["translation_engine_server"]["tokenizer"]

        self._tokenizer = spm.SentencePieceProcessor()
        self._tokenizer.load(tokenizer_path)

        gpu = int(self._gpu)
        if (gpu == -1):
            device = "cpu"
            msg = f"Loading Model -> {name} in cpu."
        else:
            device = "cuda"
            msg = f"Loading Model -> {name} in gpu."

        logging.info(msg)

        self._model = ctranslate2.Translator(model_path, device=device)

        msg = f"Model loaded"
        logging.info(msg)

        return self._model

    # Replacement of characters that p23 model does not translate properly
    async def clean(self, sentences):

        with open('language_mapping.txt') as f:
            data = f.read()
        maps = json.loads(data)
        langs = maps.values()

        replaces = {
            "–": "-",
            "“": '"',
            "”": '"',
            "≫": ">>",
            "。": ". ",
            "（": "(",
            "）": ")",
            "、": ",",
            "？": "?",
            "！": "!"
        }

        for e in replaces:
            sentences = [sent.replace(e, replaces[e]) for sent in sentences]

        for lang in langs:
            sentences = [sent.replace(
                lang, "") if lang in sent else sent for sent in sentences]

        return sentences

    async def process_batch(self, batch: List, src_lang: str, tgt_lang: str, lock: Lock = None):

        srcs = []
        segs = []
        ans = []

        no_trans_ind = []
        no_trans_trad = []

        beam_size = 5
        batch_size = 4096  # * 2

        for i, src in enumerate(batch):
            seg = Seg(src)

            # Model can not translate only spaces, new lines, tabs...
            if src.strip(NO_LONELY_TRANSLATABLE_CHARS) == "":
                no_trans_ind.append(i)
                no_trans_trad.append(seg.src)

            else:
                print(seg.src)
                await self._pipeline.preprocess(seg)
                if src_lang == "jpn_Jpan":
                    seg.src = await self.clean(seg.src)
                srcs.append(seg.src)
                print(seg.src)

            segs.append(seg)

         # If there is nothing to translate skip translation
        if len(no_trans_ind) != len(batch):

            target_prefix = [[tgt_lang]] * len(srcs)
            # Subword the source sentences
            source_sents_subworded = self._tokenizer.encode(srcs, out_type=str)
            source_sents_subworded = [sent + ["</s>", src_lang]
                                      for sent in source_sents_subworded]
            # Translate the source sentences
            while batch_size >= 64:
                try:
                    translations = self._model.translate_batch(
                            source_sents_subworded, batch_type="tokens", max_batch_size=batch_size,
                            beam_size=beam_size, target_prefix=target_prefix, replace_unknowns=True
                    )
                    batch_size = 0
                except RuntimeError as e:
                    logging.info(e)
                    msg = f"Tokens batch size is too large, reducing it from {batch_size} to {batch_size//2}."
                    logging.info(msg)
                    with open("batch_size_problems.log", "a") as f:
                        f.write(msg+"\n")
                        f.write("MAX CHARACTERS SENTENCE:  " + str(len(max(batch, key=len)))+"\n")
                        f.write("LEN BATCH TO TRANSLATE: " + str(len(batch))+"\n")
                        f.write(str(batch)+"\n")
                    batch_size = batch_size // 2

            translations = [translation.hypotheses[0][:]
                            for translation in translations]

            # Desubword the target sentences
            translations_desubword = self._tokenizer.decode(translations)
            res = [sent[len(tgt_lang)+1:].strip()
                for sent in translations_desubword]

            translations = [sent.replace("eng_Latn", "") for sent in res]

        # We add back eliminated alements
        for e, trad in zip(no_trans_ind, no_trans_trad):
            translations.insert(e, trad)
        
        for translation, seg in zip(translations, segs):
            seg.tgt_raw = translation
            seg.tgt = seg.tgt_raw
            if seg.tgt_raw.strip(NO_LONELY_TRANSLATABLE_CHARS) != "":
                await self._pipeline.postprocess(seg)
            ans.append(seg.tgt)
            logging.info(
                f"Translated -> {seg.src_raw} -> {seg.src} "
                f"-> {seg.tgt_raw} -> {seg.tgt}"
            )

        logging.info(f"BATCH LEN {len(res)}")

        for src, result in zip(srcs, ans):
            logging.info(
                f"Translated: {src} -> {result}"
            )

        return ans

    @classmethod
    def setup_log(cls, log_file: str = None, dbug: bool = None):
        hdlrs = [logging.StreamHandler()]
        if log_file is not None:
            hdlrs.append(logging.FileHandler(log_file))
        cls.lvl = logging.DEBUG if dbug else logging.INFO
        logging.basicConfig(
            handlers=hdlrs,
            level=cls.lvl,
            format="%(asctime)s :: %(levelname)s :: %(message)s",
        )


#  async def process_batch(self, batch: List, src_lang: str, tgt_lang: str, lock: Lock = None):

#         beam_size = 5
#         batch_size = 4096 #* 2

#         # Translate a list of sentences
#         source_sents = [sent.strip() for sent in batch]

#         # We have seen that Japanase, as src, does not perform well if we do the replacement
#         if src_lang == "jpn_Jpan":
#             source_sents = await self.clean(source_sents)

#         target_prefix = [[tgt_lang]] * len(source_sents)

#         # Subword the source sentences
#         source_sents_subworded = self._tokenizer.encode(source_sents, out_type=str)
#         source_sents_subworded = [sent + ["</s>", src_lang] for sent in source_sents_subworded]

#         # Translate the source sentences
#         while batch_size >= 64:
#             try:
#                 translations = self._model.translate_batch(
#                         source_sents_subworded, batch_type="tokens", max_batch_size=batch_size,
#                         beam_size=beam_size, target_prefix=target_prefix, replace_unknowns=True
#                 )
#                 batch_size = 0
#             except RuntimeError as e:
#                 logging.info(e)
#                 msg = f"Tokens batch size is too large, reducing it from {batch_size} to {batch_size//2}."
#                 logging.info(msg)
#                 with open("batch_size_problems.log", "a") as f:
#                     f.write(msg+"\n")
#                     f.write("MAX CHARACTERS SENTENCE:  " + str(len(max(batch, key=len)))+"\n")
#                     f.write("LEN BATCH TO TRANSLATE: " + str(len(batch))+"\n")
#                     f.write(str(batch)+"\n")
#                 batch_size = batch_size // 2


#         translations = [translation.hypotheses[0][:] for translation in translations]

#         # Desubword the target sentences
#         translations_desubword = self._tokenizer.decode(translations)
#         res = [sent[len(tgt_lang)+1:].strip() for sent in translations_desubword]

#         res = [sent.replace("eng_Latn", "") for sent in res]

#         logging.info(f"BATCH LEN {len(res)}")

#         for src, result in zip(source_sents, res):
#             logging.info(
#                 f"Translated: {src} -> {result}"
#             )

#         return res
