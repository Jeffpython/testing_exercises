import pytest

from functions.level_4.five_extra_fields import fetch_app_config_field, fetch_extra_fields_configuration


def test__fetch_app_config_field__returns_field_value(make_file):
    content = '''
    [tool:app-config]
    field=value
    '''
    filepath = make_file(content=content, format='ini')
    assert fetch_app_config_field(filepath, 'field') == 'value'


def test__fetch_app_config_field__returns_none_if_field_is_missing(make_file):
    content = '''
    [tool:app-config]
    other_field=value
    '''
    filepath = make_file(content=content, format='ini')
    assert fetch_app_config_field(filepath, 'field') is None


def test__fetch_app_config_field__returns_none_if_file_is_missing(make_file):
    filepath = ''
    assert fetch_app_config_field(filepath, '') is None


def test__fetch_extra_fields_configuration__returns_empty_dict_if_extra_fields_is_missing(make_file):
    content = '''
    [tool:app-config]
    '''
    filepath = make_file(content=content, format='ini')
    assert fetch_extra_fields_configuration(filepath) == {}
