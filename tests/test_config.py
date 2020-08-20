from configger import BasicConfig, SingleConfig
from configger.field import DefaultConfigField


def test_single_config_yaml():
    config = SingleConfig('config.yml')
    assert config['my-name'] == 'Bob'
    assert config['my-age'] == 18


def test_basic_config_yaml():
    config = BasicConfig('config.yml')
    assert config['my-name'] == 'Bob'
    assert config['my-age'] == 18


def test_single_config_json():
    config = SingleConfig('config.json')
    assert config['my-name'] == 'Bob'
    assert config['my-age'] == 18


def test_basic_config_json():
    config = BasicConfig('config.json')
    assert config['my-name'] == 'Bob'
    assert config['my-age'] == 18


def test_add_field_to_single_config_yaml():
    config = SingleConfig('config.yml')
    config['owner'] = 'Mike'
    assert config['owner'] == 'Mike'


def test_add_field_to_basic_config_yaml():
    config = SingleConfig('config.json')
    config['owner'] = 'Mike'
    assert config['owner'] == 'Mike'


def test_override_field_to_single_config_yaml():
    config = SingleConfig('config.yml')
    config['my-name'] = 'Mike'
    assert config['my-name'] == 'Mike'


def test_override_field_to_basic_config_yaml():
    config = SingleConfig('config.json')
    config['my-name'] = 'Mike'
    assert config['my-name'] == 'Mike'


def test_creation_single_config_yaml():
    config = SingleConfig('config.yml')
    config['my-name'] = 'Mike'
    config = SingleConfig()
    assert config['my-name'] == 'Mike'
