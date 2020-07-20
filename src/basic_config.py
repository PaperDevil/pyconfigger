"""
TODO:
    - Реализовать все функции SingleConfig
        - Наследовать SingleConfig от BasicConfig
    - Функция обновления конфига (замены файла)
    - Добавление новых полей в конфиг
"""

from pathlib import Path
from .file_worker import such_a_type, use_list, config_to_string


class BasicConfig:

    name: str = ...

    config_data: dict = None
    config_type: str = None

    _show_config = False  # Shows config with creation/updating
    _show_uses_modules = False  # Show modules using BasicConfig

    def __init__(self, config_name: str):
        self.get_config(config_name)

    def get_config(self, filename: str, config_name: str = None,
                   show_config: bool = False, show_uses_modules: bool = False):
        """Function for filling the config from JSON, YML"""
        self._show_config = show_config
        self._show_uses_modules = show_uses_modules

        if config_name is None:
            self.name = Path(filename).stem
        else: self.name = config_name

        _config_type = such_a_type(filename)
        self.config_type = _config_type
        use_list[_config_type](self, filename)  # Filling in the config

    def __repr__(self):
        return f"SingeConfig - {self.name}\n\n{config_to_string(self)}"

    def __getitem__(self, item):
        return self.config_data[item]
