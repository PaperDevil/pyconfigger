"""
TODO:
    - Реализовать все функции SingleConfig
        - Наследовать SingleConfig от BasicConfig
    - Функция обновления конфига (замены файла)
"""

from pathlib import Path
from .file_workers import such_a_type, use_list, config_to_string
from .fields import DefaultConfigField


def showing_config(decorate):
    def wrapper(cls, *args, **kwargs):
        decorate(cls, *args, **kwargs)
        if cls.show_config:
            print(cls)
    return wrapper


class BasicConfig:
    """
    Basic realisation of Configger.
    Can have multiple instances.
    """

    name: str = ...

    config_data: dict = None
    config_type: str = None

    _show_config = False  # Shows config with creation/updating
    _show_uses_modules = False  # Show modules using BasicConfig

    def __init__(self, config_name: str, show_config: bool = False,
                 show_uses_modules: bool = False):
        self.show_config = show_config
        self.show_uses_modules = show_uses_modules
        self.set_config(config_name)

    @showing_config
    def set_config(self, filename: str, config_name: str = None):
        """Function for filling the config from JSON, YML"""

        if config_name is None:
            self.name = Path(filename).stem
        else: self.name = config_name

        _config_type = such_a_type(filename)
        self.config_type = _config_type
        use_list[_config_type](self, filename)  # Filling in the config

    @property
    def show_config(self):
        """Show config data when config use or update"""
        return self._show_config

    @show_config.setter
    def show_config(self, value: bool):
        self._show_config = value

    def __call__(self, field: str, algorithm: str = None):
        return self.config_data[field]

    def __repr__(self):
        return f"SingeConfig - {self.name}\n\n{config_to_string(self)}"

    def __getitem__(self, item: str):
        return self.config_data[item].value

    def __setitem__(self, key: str, value: DefaultConfigField):
        self.config_data[key] = value
