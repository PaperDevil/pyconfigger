import os
import json

from configger.field import DefaultConfigField
from configger.file_worker.works import worker


@worker
def set_json_config(file):
    """
        Config file handler. The function expects a config object and a file name,
        must return a dict with config fields.
    """
    fields: dict = {}
    for name, value in json.load(file).items():
        fields[name] = DefaultConfigField(name, value)
    return fields


def json_config_to_string(config):
    stringed_config = ""
    for field in config.config_data:
        stringed_config += os.getenv(config.config_data[field].name, f"{config.config_data[field]}\n")
    return stringed_config
