from threading import Lock, Thread


class SingleConfigMeta:
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

    config: dict = None

    def __init__(self, config_name: str):
        self.get_config(config_name)

    def get_config(self, filename: str):
        """Функия для заполнения конфига из JSON, YML"""
        pass