from langchain.llms import HuggingFaceHub
from huggingface_hub import hf_hub_download
from langchain.llms import LlamaCpp

from constants import (
    MODELS_PATH,
    CONTEXT_WINDOW_SIZE,
    N_BATCH,
    MAX_NEW_TOKENS,
)


def load_model(
    model_id: str = "tiiuae/falcon-180B-chat",
    model_basename: str = "pytorch_model.bin",
    loader_type: str = "hf_hub",
):
    if loader_type.lower() == "hf_hub":
        model = HuggingFaceHub(
            repo_id=model_id,
            model_kwargs={
                "max_tokens": 4000,
                "max_length": 64,
                "temperature": 0.1,
            },
        )
    else:
        model_path = hf_hub_download(
            repo_id=model_id,
            filename=model_basename,
            resume_download=True,
            cache_dir=MODELS_PATH,
        )
        kwargs = {
            "model_path": model_path,
            "n_ctx": CONTEXT_WINDOW_SIZE,
            "max_tokens": MAX_NEW_TOKENS,
            "n_batch": N_BATCH,  # set this based on your GPU & CPU RAM
        }
        # if device_type.lower() == "mps":
        #     kwargs["n_gpu_layers"] = 1
        # if device_type.lower() == "cuda":
        #     kwargs["n_gpu_layers"] = N_GPU_LAYERS  # set this based on your GPU

        model = LlamaCpp(**kwargs)

    return model
