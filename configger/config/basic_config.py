from os import getenv
from pathlib import Path
from functools import lru_cache

from configger.file_worker import such_a_type, use_list, config_to_string
from configger.field import DefaultConfigField


class BasicConfig:
    """
    Basic realisation of Configger.
    Can have multiple instances.
    """

    name: str = None
    file: str = None

    config_data: dict = None
    config_type: str = None

    show_config = False
    show_uses_modules = False  # Show modules using BasicConfig TODO
    use_environ = False

    def __init__(self,
                 filename: str = None,
                 show_config: bool = False,
                 show_uses_modules: bool = False,
                 use_environ: bool = False):

        self.show_config = show_config
        self.show_uses_modules = show_uses_modules
        self.user_environ = use_environ

        if filename:
            self.set_config(filename)

    def set_config(self, filename: str, config_name: str = None):
        """Function for filling the config from JSON, YML"""

        if self.show_config:
            print(self)

        if config_name is None:
            self.name = Path(filename).stem
        else:
            self.name = config_name
        self.file = filename

        _config_type = such_a_type(filename)
        if _config_type is None:
            raise Exception("Config file not found or not supported!")
        self.config_type = _config_type
        use_list[_config_type](self, filename)  # Filling in the config

    def __call__(self, field: str, algorithm: str = None):
        result = None
        try:
            result = self.config_data[field]
        except KeyError as exc:
            raise KeyError("Field not found in config. "
                           "If you want get field from environment you should use config[<filed name>].")
        return result

    def __repr__(self):
        return f"BasicConfig - file: {self.file} name: {self.name}\n" \
               f"===== Config Fields =====\n" \
               f"{config_to_string(self)}" \
               f"========================="

    def __getitem__(self, item: str):
        result = None
        if self.use_environ:
            result = getenv(str(item), None)
        if item in self.config_data and result is None:
            result = self.config_data[item].value
        return result

    def __setitem__(self, key: str, value: any):
        self.config_data[key] = DefaultConfigField(key, value)
