import os, sys, yaml, json
import numpy as np

from collections import OrderedDict
from yamlordereddictloader import SafeDumper
from yamlordereddictloader import SafeLoader
from loguru import logger


def create_dir(directory):
    """
    Checks the existence of a directory, if does not exist, create a new one
    :param directory: path to directory under concern
    :return: None
    """
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            logger.success('Create directory: ' + directory)
    except OSError:
        logger.error('Create directory: ' +  directory)
        sys.exit()
    

def create_subdir(path: str, subdir_list: list):
    for subdir in subdir_list:
        subdir_path = os.path.join(path, subdir.strip('/'))
        if not os.path.exists(subdir_path):
            create_dir(subdir_path)

    
def read_yaml(file):
    return yaml.load(open(file), Loader=SafeLoader)


def write_yaml(file, content):
    """
    if file exists at filepath, overwite the file, if not, create a new file
    :param filepath: string that specifies the destination file path
    :param content: yaml string that needs to be written to the destination file
    :return: None
    """
    if os.path.exists(file):
        os.remove(file)
    create_dir(os.path.dirname(file))
    out_file = open(file, 'a')
    out_file.write(yaml.dump( content, default_flow_style= False, Dumper=SafeDumper))


def get_path(path):
    path = os.path.abspath(path)
    path = os.path.realpath(path)
    assert os.path.exists(path), logger.error('Invalid path: ' + path)
    return path

