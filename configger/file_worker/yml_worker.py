from configger.field import DefaultConfigField
from configger.file_worker.works import worker

yaml = None

@worker
def set_yml_config(file):

    """
    Config file handler. The function expects a config object and a file name,
    must return a dict with config fields.
    """

    try:
        # Import inside function bcs we want get pyyaml only when user YAML config file
        import yaml
    except ImportError:
        raise Exception("PyYAML not found, please install: pip install pyyaml")

    fields: dict = {}
    for name, value in yaml.safe_load(file).items():
        fields[name] = DefaultConfigField(name, value)
    return fields


def yml_config_to_string(config):
    stringed_config = ""
    for field in config.config_data:
        stringed_config += f"{config.config_data[field]}\n"
    return stringed_config
