from pangeamt_nlp.processor.pipeline_decoding import PipelineDecoding
from pangeamt_nlp.processor.pipeline_training import PipelineTraining
from pangeamt_nlp.truecaser.truecaser import Truecaser
from pangeamt_nlp.bpe.bpe import BPE
from pangeamt_nlp.bpe.sentencepiece import SentencePieceSegmenter
from pangeamt_nlp.tokenizer.tokenizer_factory import TokenizerFactory
from pangeamt_nlp.tokenizer.tokenizer_base import TokenizerBase
from pangeamt_nlp.seg import Seg
from typing import Dict, Tuple
import os
import logging
from logging import Logger


class Pipeline:

    def __init__(self, config: Dict) -> "Pipeline":
        self._config = config
        if "processors" not in self._config:
            self._config["processors"]={}
        self._src_lang = ""  # config["src_lang"]
        self._tgt_lang = ""  # config["tgt_lang"]
        self._decoding_pipeline = self.load_decoding_pipeline()

    async def preprocess(self, seg: Seg):
        self._decoding_pipeline.process_src(seg, logger=logging.getLogger())
       
    async def postprocess(self, seg: Seg):
        self._decoding_pipeline.process_tgt(seg, logger=logging.getLogger())

    def load_decoding_pipeline(self) -> PipelineDecoding:
        return PipelineDecoding.create_from_dict(
            self._src_lang, self._tgt_lang, self._config["processors"]
        )
