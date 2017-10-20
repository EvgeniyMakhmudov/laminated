import timeit
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


r = timeit.repeat(
    'import string; [l[char] for char in string.ascii_lowercase]',
    'from __main__ import init_data; l=init_data()',
    repeat=REPEAT,
    number=NUMBER,
)
print('Benchmark 1: getitem: {}'.format(min(r)))


r = timeit.repeat(
    'import string; [l.get_value_at_layer(char, char) for char in string.ascii_lowercase]',
    'from __main__ import init_data; l=init_data()',
    repeat=REPEAT,
    number=NUMBER,

)
print('Benchmark 2: get_value_at_layer: {}'.format(min(r)))


r = timeit.repeat(
    'import string; l.get_dict_at_layer("a")',
    'from __main__ import init_data; l=init_data()',
    repeat=REPEAT,
    number=NUMBER,

)
print('Benchmark 3: get_dict_at_layer at bottom: {}'.format(min(r)))

r = timeit.repeat(
    'import string; l.get_dict_at_layer("m")',
    'from __main__ import init_data; l=init_data()',
    repeat=REPEAT,
    number=NUMBER,

)
print('Benchmark 3: get_dict_at_layer at middle: {}'.format(min(r)))

r = timeit.repeat(
    'import string; l.get_dict_at_layer("z")',
    'from __main__ import init_data; l=init_data()',
    repeat=REPEAT,
    number=NUMBER,

)
print('Benchmark 3: get_dict_at_layer at top: {}'.format(min(r)))
