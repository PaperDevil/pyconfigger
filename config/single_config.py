from pathlib import Path
from threading import Lock, Thread

from file_worker import such_a_type, use_list, config_to_string
from config.basic_config import BasicConfig


class SingleConfigMeta(type):
    """
    Metaclass for realize multithreading singleton pattern
    """

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
        return f"SingeConfig - {self.name}\n\n{config_to_string(self)}"
