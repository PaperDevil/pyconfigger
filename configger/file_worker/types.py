from configger.file_worker.json_worker import set_json_config, json_config_to_string
from configger.file_worker.yml_worker import set_yml_config, yml_config_to_string


def such_a_type(filename: str):
    if ".yml" in filename or ".YML" in filename:
        return "YML"
    if ".json" in filename or ".JSON" in filename:
        return "JSON"


def config_to_string(config):
    if config.config_type == "YML":
        return yml_config_to_string(config)
    if config.config_type == "JSON":
        return json_config_to_string(config)


use_list = {
    'YML': set_yml_config,
    'JSON': set_json_config
}


