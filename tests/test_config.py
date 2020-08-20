import pytest

from configger import BasicConfig, SingleConfig
from configger.field import DefaultConfigField


@pytest.fixture()
def single_config_yml():
    return SingleConfig('config.yml')


@pytest.fixture()
def single_config_json():
    return SingleConfig('config.json')


@pytest.fixture()
def basic_config_yml():
    return BasicConfig('config.yml')


@pytest.fixture()
def basic_config_json():
    return BasicConfig('config.json')


def test_single_config_yaml(single_config_yml):
    assert single_config_yml['my-name'] == 'Bob'
    assert single_config_yml['my-age'] == 18


def test_basic_config_yaml(basic_config_yml):
    assert basic_config_yml['my-name'] == 'Bob'
    assert basic_config_yml['my-age'] == 18


def test_single_config_json(single_config_json):
    assert single_config_json['my-name'] == 'Bob'
    assert single_config_json['my-age'] == 18


def test_basic_config_json(basic_config_json):
    assert basic_config_json['my-name'] == 'Bob'
    assert basic_config_json['my-age'] == 18


def test_add_field_to_single_config_yaml(single_config_yml):
    single_config_yml['owner'] = 'Mike'
    assert single_config_yml['owner'] == 'Mike'


def test_add_field_to_basic_config_yaml(basic_config_yml):
    basic_config_yml['owner'] = 'Mike'
    assert basic_config_yml['owner'] == 'Mike'


def test_add_field_to_single_config_json(single_config_json):
    single_config_json['owner'] = 'Mike'
    assert single_config_json['owner'] == 'Mike'


def test_add_field_to_basic_config_json(basic_config_json):
    basic_config_json['owner'] = 'Mike'
    assert basic_config_json['owner'] == 'Mike'


def test_override_field_to_single_config_yaml(single_config_yml):
    single_config_yml['my-name'] = 'Mike'
    assert single_config_yml['my-name'] == 'Mike'


def test_override_field_to_basic_config_yaml(basic_config_yml):
    basic_config_yml['my-name'] = 'Mike'
    assert basic_config_yml['my-name'] == 'Mike'


def test_override_field_to_single_config_json(single_config_json):
    single_config_json['my-name'] = 'Mike'
    assert single_config_json['my-name'] == 'Mike'


def test_override_field_to_basic_config_json(basic_config_json):
    basic_config_json['my-name'] = 'Mike'
    assert basic_config_json['my-name'] == 'Mike'


def test_creation_single_config_yaml(single_config_yml):
    single_config_yml['my-name'] = 'Mike'
    single_config_yml = SingleConfig()
    assert single_config_yml['my-name'] == 'Mike'


def test_creation_single_config_json(single_config_json):
    single_config_json['my-name'] = 'Mike'
    single_config_json = SingleConfig()
    assert single_config_json['my-name'] == 'Mike'


def test_load_list_single_config_yaml(single_config_yml):
    assert type(single_config_yml['my-list']) == list
    assert single_config_yml['my-list'] == ['apple', 'orange', 'banana']


def test_load_list_basic_config_yaml(basic_config_yml):
    assert type(basic_config_yml['my-list']) == list
    assert basic_config_yml['my-list'] == ['apple', 'orange', 'banana']


def test_load_list_single_config_json(single_config_json):
    assert type(single_config_json['my-list']) == list
    assert single_config_json['my-list'] == ['apple', 'orange', 'banana']


def test_load_list_basic_config_json(basic_config_json):
    assert type(basic_config_json['my-list']) == list
    assert basic_config_json['my-list'] == ['apple', 'orange', 'banana']


def test_add_list_to_single_config_yaml(single_config_yml):
    single_config_yml['new-list'] = ['Bob', 'Ann', 'Joe']
    assert type(single_config_yml['new-list']) == list
    assert single_config_yml['new-list'] == ['Bob', 'Ann', 'Joe']


def test_add_list_to_basic_config_yaml(basic_config_yml):
    basic_config_yml['new-list'] = ['Bob', 'Ann', 'Joe']
    assert type(basic_config_yml['new-list']) == list
    assert basic_config_yml['new-list'] == ['Bob', 'Ann', 'Joe']


def test_add_list_to_single_config_json(single_config_json):
    single_config_json['new-list'] = ['Bob', 'Ann', 'Joe']
    assert type(single_config_json['new-list']) == list
    assert single_config_json['new-list'] == ['Bob', 'Ann', 'Joe']


def test_add_list_to_basic_config_json(basic_config_json):
    basic_config_json['new-list'] = ['Bob', 'Ann', 'Joe']
    assert type(basic_config_json['new-list']) == list
    assert basic_config_json['new-list'] == ['Bob', 'Ann', 'Joe']