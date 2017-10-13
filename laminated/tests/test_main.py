from ..laminated import Laminated


def test():
    l = Laminated()
    l.add_layer(
        {
            'a': 'A',
            'b': '',
        }
    )
    l.add_layer(
        name='fix',
        data={
            'b': 'B',
        }
    )

    assert len(list(l.get_layers())) == 2

    assert l['b'] == 'B'
    assert l['a'] == 'A'
