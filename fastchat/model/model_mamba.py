from types import SimpleNamespace
import warnings

from mamba_ssm.models.mixer_seq_simple import MambaLMHeadModel


class MambaModel:
    def __init__(self, model_path):
        warnings.warn("Experimental support for Mamba.")
        
        self.config = SimpleNamespace(is_encoder_decoder=False)
        self.model = MambaLMHeadModel.from_pretrained(model_path)
        self.tokenizer = None
        self.model_path = model_path

    def to(self, target):
        assert target == "cuda"

    def generate(self, input_ids, do_sample, temperature, max_new_tokens, top_k=1, top_p=0.0, min_p=0.0):
        return self.model.generate(input_ids, max_new_tokens, top_k, top_p, min_p, temperature)
