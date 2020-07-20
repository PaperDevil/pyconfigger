"""
TODO:
    - Отрефакторить функцию заполнения под новые классы ConfigFields
    - Создать декоратор для функций set_some_config для задачи выше
"""

import yaml


def set_yml_config(config, filename: str):
    with open(filename) as file:
        config.config = yaml.safe_load(file)
        return config.config


def yml_config_to_string(config):
    return yaml.dump(config.config)
