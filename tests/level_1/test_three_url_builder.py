from functions.level_1.three_url_builder import build_url


def test_build_url__blank_params():
    assert build_url('http://google.com', 'catalog') == 'http://google.com/catalog'
    # assert build_url('http://google.com', 'catalog', '') == 'http://google.com/catalog'


def test_build_url__params_with_one_value():
    params = {'key': 'value'}
    assert build_url('http://google.com', 'catalog', params) == 'http://google.com/catalog?key=value'


def test_build_url__params_with_two_value():
    params = {'key1': 'value1', 'key2': 'value2'}
    assert build_url('http://google.com', 'catalog', params) == 'http://google.com/catalog?key1=value1&key2=value2'
