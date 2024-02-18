# following two lines are used in testing
import sys, os, shutil
sys.path.append(os.getcwd())

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from langchain_wrapper.llm.llm import build_llm


def test_vllm_llama2_7b():
    llm = build_llm(llm_yaml='./examples/vllm-llama2-7b.yaml')
    template = """Question: {question}
    Answer: Let's think step by step."""
    prompt = PromptTemplate.from_template(template)
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    question = "I am sad now, and I want to listen to a song."
    print(llm_chain.invoke(question)['text'])


def test_vllm_mistral_7b():
    llm = build_llm(llm_yaml='./examples/vllm-mistral-7b.yaml')
    template = """Question: {question}
    Answer: Let's think step by step."""
    prompt = PromptTemplate.from_template(template)
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    question = "I am sad now, and I want to listen to a song."
    print(llm_chain.invoke(question)['text'])


if __name__ == '__main__':
    test_vllm_llama2_7b()
    test_vllm_mistral_7b()

