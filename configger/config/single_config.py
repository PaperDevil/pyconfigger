from threading import Lock
from abc import ABCMeta

from configger.file_worker import config_to_string
from configger.config.basic_config import BasicConfig


class SingleConfigMeta(ABCMeta):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingleConfigMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingleConfig(BasicConfig, metaclass=SingleConfigMeta):

    def __repr__(self):
        return f"SingleConfig - file: {self.file} name: {self.name}\n" \
               f"===== Config Fields =====\n" \
               f"{config_to_string(self)}" \
               f"========================="
