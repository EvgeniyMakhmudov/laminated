import pytest

from ..laminated import Laminated


@pytest.fixture
def l_minimum():
    l = Laminated()
    l.add_layer(
        {
            'a': 'A',
            'b': '',
        },
        name='base'
    )
    l.add_layer(
        name='fix',
        data={
            'b': 'B',
        }
    )
    l.add_layer(
        data={
            'c': 'C',
        }
    )
    return l


def test__getitem__(l_minimum):
    assert l_minimum['b'] == 'B'
    assert l_minimum['a'] == 'A'


@pytest.mark.xfail(raises=KeyError)
def test__getitem__fail(l_minimum):
    l_minimum['z']


def test_get_layer_item(l_minimum):
    assert l_minimum.get_layer_item('base', 'b') == ''
    assert l_minimum.get_layer_item('fix', 'b') == 'B'
    assert l_minimum.get_layer_item('fix', 'a')

    top_name = l_minimum._names[0]
    assert l_minimum.get_layer_item('fix', 'a') == l_minimum.get_layer_item(top_name, 'a')


@pytest.mark.xfail(raises=KeyError)
def test_get_layer_item_fail(l_minimum):
    l_minimum.get_layer_item('base', 'c')
