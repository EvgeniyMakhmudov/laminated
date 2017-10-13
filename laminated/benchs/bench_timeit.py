import timeit
import string
from random import randint

import sys
sys.path.append('.')

import laminated  # noqa


def init_data():
    l = laminated.Laminated()
    for char in string.ascii_lowercase:
        l.add_layer(
            name=char,
            data={c: randint(500, 1000) for c in string.ascii_lowercase}
        )
    return l

r = timeit.repeat(
    'import string; [l[char] for char in string.ascii_lowercase]',
    'from __main__ import init_data; l=init_data()',
    repeat=10,
    number=1000,
)
print(min(r))
