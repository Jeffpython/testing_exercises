from functions.level_1.three_url_builder import build_url


def test_build_url():
    params_1 = {'key': 'value'}
    params_2 = {'key1': 'value1', 'key2': 'value2'}
    assert build_url('http://google.com', 'catalog') == 'http://google.com/catalog'
    assert build_url('http://google.com', 'catalog', params_1) == 'http://google.com/catalog?key=value'
    assert build_url('http://google.com', 'catalog', params_2) == 'http://google.com/catalog?key1=value1&key2=value2'
