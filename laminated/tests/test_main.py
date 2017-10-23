import pytest


def test__getitem__(l_minimum):
    assert l_minimum['b'] == 'B'
    assert l_minimum['a'] == 'A'


def test__getitem__fail(l_minimum):
    with pytest.raises(KeyError):
        l_minimum['z']


def test_get_value_at_layer(l_minimum):
    assert l_minimum.get_value_at_layer('base', 'b') == ''
    assert l_minimum.get_value_at_layer('fix', 'b') == 'B'
    assert l_minimum.get_value_at_layer('fix', 'a')
    assert l_minimum.get_value_at_layer('fix', 'a') == l_minimum['a']


def test_get_value_at_layer_fail(l_minimum):
    with pytest.raises(KeyError):
        l_minimum.get_value_at_layer('base', 'c')
