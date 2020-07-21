"""
TODO:
    - Редактировать функцию yml_config_to_string для красивого вывода
"""

import yaml
from ..fields import DefaultConfigField
from .works import worker


@worker
def set_yml_config(file):
    """
    Config file handler. The function expects a config object and a file name,
    must return a dict with config fields.
    """
    fields: dict = {}
    for name, value in yaml.safe_load(file).items():
        fields[name] = DefaultConfigField(name, value)
    return fields


def yml_config_to_string(config):
    stringed_config = ""
    for field in config.config_data:
        stringed_config += f"{config.config_data[field]}\n"
    return stringed_config
