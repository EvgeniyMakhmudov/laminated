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


def test(l_minimum):
    assert len(list(l_minimum.get_layers_names())) == 3

    assert l_minimum['b'] == 'B'
    assert l_minimum['a'] == 'A'


def test_get_layer_item(l_minimum):
    assert l_minimum.get_layer_item('base', 'b') == ''
    assert l_minimum.get_layer_item('fix', 'b') == 'B'
    assert l_minimum.get_layer_item('fix', 'a')
