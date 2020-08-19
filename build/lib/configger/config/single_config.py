from threading import Lock

from configger.file_worker import config_to_string
from configger.config.basic_config import BasicConfig
from configger.fishes import fish_json_path


class SingleConfigMeta(type):

    _instances = {}

    _lock: Lock = Lock()  # Lock activate in first thread

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class SingleConfig(BasicConfig, metaclass=SingleConfigMeta):

    def __repr__(self):
        return f"SingleConfig - file: {self.file} name: {self.name}\n" \
               f"===== Config Fields =====\n" \
               f"{config_to_string(self)}" \
               f"========================="
