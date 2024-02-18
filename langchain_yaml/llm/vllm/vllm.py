from langchain_community.llms import VLLM

from langchain_yaml.utils.utils import create_dir


def build(llm_cfg):
    model_src = llm_cfg['model_src']['hugging_face']
    model_dst = llm_cfg['model_dst']['local']
    max_new_tokens = llm_cfg['max_new_tokens']
    vllm_kwargs = llm_cfg['vllm_kwargs']

    # local model path
    create_dir(model_dst)

    # create model: https://github.com/langchain-ai/langchain/blob/master/libs/community/langchain_community/llms/vllm.py
    llm = VLLM(
        model=model_src,
        download_dir=model_dst,
        trust_remote_code=True,
        max_new_tokens=max_new_tokens,
        vllm_kwargs=vllm_kwargs,
    )

    return llm

