import json


def set_json_config(config, filename: str):
    with open(filename) as file:
        config.config = json.load(file)
        return config.config


def json_config_to_string(config):
    return json.dumps(config.config, indent=2)
