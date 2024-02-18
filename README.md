# langchain_yaml
This is a framework to ease the deployment of llms with langchain. The goal is to use yaml files for configurations.

## Installation
1. ```conda create --name lcy python=3.11```
2. ```conda activate lcy```
3. ```pip install vllm```
4. ```conda install -c conda-forge langchain pyyaml yamlordereddictloader pytest loguru openai```
5. In the root directory, ```python3 -m pip install -e . --no-deps```
