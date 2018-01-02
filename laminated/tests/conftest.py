import pytest

from laminated import Laminated


@pytest.fixture
def l_minimum():
    lam = Laminated()
    lam.add_layer(
        {
            'a': 'A',
            'b': '',
        },
        name='base'
    )
    lam.add_layer(
        name='fix',
        data={
            'b': 'B',
        }
    )
    lam.add_layer(
        data={
            'c': 'C',
        }
    )
    return lam
