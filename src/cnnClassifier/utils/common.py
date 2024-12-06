import os
import sys
import yaml
import base64
import json
import joblib
from typing import Any
from pathlib import Path
from box import Box
from ensure import ensure_annotations
from cnnClassifier import logger, CustomExceptionHandling


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> Box:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml, 'r') as f:
            yaml_content = yaml.safe_load(f)
            logger.info(f'{path_to_yaml} Yaml file loaded successfully')
            return Box(yaml_content)
    except Exception as e:
        raise CustomExceptionHandling(e, sys)


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for dir_path in path_to_directories:
        os.makedirs(dir_path, exist_ok=True)
        if verbose:
            logger.info(f'Created directory at {dir_path}')


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, 'w') as json_output_file:
        json.dump(data, json_output_file, indent=4)
        logger.info(f'Json data saved successfully to {path}')


@ensure_annotations
def load_json(path: Path) -> Box:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path, 'r') as json_file:
        json_content = json.load(json_file)
        logger.info(f'Json file {path} read successfully ')
        return (Box(json_content))


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(data, path)
    logger.info(f'Data saved to binary file {path} successfully')


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    binary_content = joblib.load(path)
    logger.info(f'Binary data loaded successfully from {path}')
    return binary_content


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = f'{round(os.path.getsize(path)/1024,2)} KB {path}'
    return size_in_kb


def decodeImage(imgstring, fileName):
    pass


def encodeImageIntoBase64(croppedImagePath):
    pass
