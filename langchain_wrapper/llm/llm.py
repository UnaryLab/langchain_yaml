import os, sys
import importlib.util

from langchain_wrapper.utils.utils import read_yaml, get_path
from loguru import logger


def build_llm(llm_yaml: str = None):
    """
    This function builds and returns an LLM from an 'llm.yaml' file
    """
    llm_path = get_path(llm_yaml)
    llm_cfg = read_yaml(llm_path)
    assert 'llm' in llm_cfg.keys(), logger.error('Missing <llm> in LLM configuration at <' + llm_path + '>.')
    llm_cfg = llm_cfg['llm']

    # framework has to be specified
    assert 'framework' in llm_cfg.keys(), logger.error('Missing <framework> in LLM configuration at <' + llm_path + '>.')
    framework = llm_cfg['framework'].lower()

    # find proper framework to build the llm
    dst_file = os.path.join(os.path.dirname(__file__), framework, framework + '.py')
    spec = importlib.util.spec_from_file_location('build_llm_with' + framework, dst_file)
    module_py = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module_py
    spec.loader.exec_module(module_py)

    llm = module_py.build(llm_cfg)

    return llm

