"""
TODO:
    - Оптимизировать модуль
    - Адаптировать SingleConfig под BasicConfig
"""


from pathlib import Path
from threading import Lock, Thread
from .file_workers import such_a_type, use_list, config_to_string


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


class SingleConfig(metaclass=SingleConfigMeta):
    """
    Класс пораждающий инстанс конфига, что позволяет использовать единный конфиг во всём проекте
    """

    name: str = None

    config: dict = None
    config_type: str = None

    _show_config = False  # Выводит конфиг при создании/заполнении
    _show_uses_modules = False  # Выводит пути модулей использующих конфиг

    def __init__(self, config_name: str):
        self.get_config(config_name)

    def get_config(self, filename: str):
        """Функия для заполнения конфига из JSON, YML"""
        self.name = Path(filename).stem

        _config_type = such_a_type(filename)
        self.config_type = _config_type
        use_list[_config_type](self, filename)

    def __repr__(self):
        return f"SingeConfig - {self.name}\n\n{config_to_string(self)}"

    def __getitem__(self, item):
        return self.config[item]
