from langchain_wrapper.utils.utils import create_dir
from langchain_community.llms import VLLMOpenAI


def build(llm_cfg):
    openai_api_key = llm_cfg['openai_api_key']
    openai_api_base = llm_cfg['openai_api_base']
    model_name = llm_cfg['model_name']
    model_kwargs = llm_cfg['model_kwargs']

    # local model path
    # create_dir(model_dst)

    # create model: https://github.com/langchain-ai/langchain/blob/master/libs/community/langchain_community/llms/vllm.py
    llm = VLLMOpenAI(
        openai_api_key=openai_api_key,
        openai_api_base=openai_api_base,
        model_name=model_name,
        model_kwargs=model_kwargs,
    )

    return llm

