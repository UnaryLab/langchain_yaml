# following two lines are used in testing
import sys, os, shutil
sys.path.append(os.getcwd())

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from langchain_yaml.llm import build_llm


def test_vllmopenai_mistral_7b():
    print('To run this test, be sure to set up an OpenAI compatible server first')
    print('For example, <python -m vllm.entrypoints.openai.api_server --model mistralai/Mistral-7B-v0.1 --max-model-len 2048>')
    print('More can be found here: https://docs.vllm.ai/en/latest/getting_started/quickstart.html')
    
    llm = build_llm(llm_yaml='./examples/vllm-openai-mistral-7b.yaml')
    template = """Question: {question}
    Answer: Let's think step by step."""
    prompt = PromptTemplate.from_template(template)
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    question = "I am sad now, and I want to listen to a song."
    print(llm_chain.invoke(question)['text'])


if __name__ == '__main__':
    test_vllmopenai_mistral_7b()

