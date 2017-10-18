import pytest


@pytest.mark.parametrize('layer_name, target', [
    ['base', {'a': 'A', 'b': ''}],
    ['fix', {'a': 'A', 'b': 'B'}],
])
def test_get_dict_at_layer(l_minimum, layer_name, target):
    assert l_minimum.get_dict_at_layer(layer_name) == target


@pytest.mark.xfail(raises=ValueError)
def test_get_dict_at_layer_fail(l_minimum):
    l_minimum.get_dict_at_layer('not_exists')
