import string
from random import randint

import sys
sys.path.append('.')

import laminated  # noqa


REPEAT = 10
NUMBER = 10000


def init_data():
    l = laminated.Laminated()
    for char in string.ascii_lowercase:
        l.add_layer(
            name=char,
            data={c: randint(500, 1000) for c in string.ascii_lowercase}
        )
    return l

print('Benchmark 1: sizeof: {}'.format(sys.getsizeof(init_data)))
