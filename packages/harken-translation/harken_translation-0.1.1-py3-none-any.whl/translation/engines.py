import sentencepiece as spm
import ctranslate2
import re
import json
import os
import structlog

logger = structlog.getLogger(__name__)


class EngineENUStoENUK:

    def __init__(self, url):
        logger.info('>>> Loading UK-US dictionary... <<<')
        self.repl_dict = {}
        self.url = url
        tmp_dict = json.loads(open(url, 'r').read())
        for key, value in tmp_dict.items():
            self.repl_dict[key] = value
            self.repl_dict[key.upper()] = value.upper()
            self.repl_dict[key.title()] = value.title()
            self.repl_dict[key.capitalize()] = value.capitalize()
        self.pattern = '|'.join(r'\b%s\b' % re.escape(s) for s in self.repl_dict)
        logger.info('>>> Loaded UK-US dictionary... <<<')

    def replace(self, match):
        return self.repl_dict[match.group(0)]

    def replace_us_uk(self, sentence):
        return re.sub(self.pattern, self.replace, sentence)

    def sample(self, texts, **kwargs):
        return [self.replace_us_uk(text) for text in texts]


class EngineNLLB200():

    def __init__(self, url, prefix, suffix, device="cuda"):
        self.prefix = prefix
        self.suffix = suffix
        self.sp = spm.SentencePieceProcessor()
        self.sp.load(os.path.join(url, "flores200_sacrebleu_tokenizer_spm.model"))
        self.translator = ctranslate2.Translator(url, device)

    def sample(self, texts, **kwargs):
        src_lang = kwargs.get("src_lang", "")
        tgt_lang = kwargs.get("tgt_lang", "")
        beam_size = kwargs.get("beam_size", 5)
        source_sentences = [sent.strip() for sent in texts]
        target_prefix = [[tgt_lang]] * len(source_sentences)
        # Subword the source sentences
        source_sents_subworded = self.sp.encode_as_pieces(source_sentences)
        source_sents_subworded = [[src_lang] + sent + ["</s>"] for sent in source_sents_subworded]
        logger.info("Sources:", texts)
        logger.info("Target Language:", tgt_lang)
        # Translate the source sentences
        translations_subworded = self.translator.translate_batch(source_sents_subworded, batch_type="tokens",
                                                                 max_batch_size=2024,
                                                                 beam_size=beam_size,
                                                                 target_prefix=target_prefix)
        translations_subworded = [translation.hypotheses[0] for translation in translations_subworded]
        for translation in translations_subworded:
            if tgt_lang in translation:
                translation.remove(tgt_lang)
        # Desubword the target sentences
        translations = self.sp.decode(translations_subworded)
        logger.info("Translations:", translations)
        return translations


class EngineC2Translate:

    def __init__(self, url, prefix, suffix):
        logger.info("Loading Sentence Piece Model")
        self.sp = spm.SentencePieceProcessor()
        self.sp.load(os.path.join(url, "sentencepiece.bpe.model"))
        logger.info("Loading Model")
        self.translator = ctranslate2.Translator(url, device="cuda")
        self.prefix = prefix
        self.suffix = suffix

    def sample(self, texts, **kwargs):
        sources = self.sp.encode(texts, out_type=str)
        sources = [[self.prefix] + source for source in sources]
        target_prefix = [[self.suffix] for _ in sources]
        logger.info("******* Beam -> {} *******".format(kwargs.get("beam", 5)))
        results = self.translator.translate_batch(sources,
                                                  target_prefix=target_prefix,
                                                  return_attention=True,
                                                  beam_size=kwargs.get("beam", 5))
        outputs = [self.sp.decode(result.hypotheses[0][1:]) for result in results]
        return outputs


__all__ = ["EngineENUStoENUK", "EngineNLLB200", "EngineC2Translate"]
