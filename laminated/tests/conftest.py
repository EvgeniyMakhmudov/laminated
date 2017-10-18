import pytest

from laminated import Laminated


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
