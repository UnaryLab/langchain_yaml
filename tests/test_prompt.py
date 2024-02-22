# following two lines are used in testing
import sys, os, shutil
sys.path.append(os.getcwd())

from langchain.chains import LLMChain

from langchain_yaml.llm import build_llm
from langchain_yaml.prompt import build_prompt


def test_prompt():
    llm = build_llm(llm_yaml='./examples/vllm-llama2-7b.yaml')
    prompt = build_prompt(prompt_yaml='./examples/prompt-template-1.yaml')
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    question = "I am sad now, and I want to listen to a song."
    print(llm_chain.invoke(question)['text'])


if __name__ == '__main__':
    test_prompt()

