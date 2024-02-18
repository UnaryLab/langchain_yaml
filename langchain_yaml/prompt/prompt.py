import os, sys
import importlib.util

from loguru import logger
from langchain.prompts import PromptTemplate

from langchain_yaml.utils.utils import read_yaml, get_path


def build_prompt(prompt_yaml: str = None):
    """
    This function builds and returns a prompt from a 'prompt.yaml' file
    """
    prompt_path = get_path(prompt_yaml)
    prompt_cfg = read_yaml(prompt_path)
    assert 'prompt' in prompt_cfg.keys(), logger.error('Missing <prompt> in prompt configuration at <' + prompt_path + '>.')
    prompt_cfg = prompt_cfg['prompt']
    # template is a string, so formulate the input yaml as string.
    prompt_template= prompt_cfg['template']
    
    # build prompt template
    prompt = PromptTemplate.from_template(prompt_template)

    return prompt

