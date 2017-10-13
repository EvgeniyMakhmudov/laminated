from uuid import uuid4
from collections import OrderedDict


class Laminated:
    def __init__(self):
        self._data = OrderedDict()
        self._index = OrderedDict()
        self._names = set()

    def __getitem__(self, item):
        for key in sorted(self._data.keys(), reverse=True):
            if item in self._data[key]:
                return self._data[key][item]
        else:
            self._data[key][item]

    def add_layer(self, data, name=None):
        if name is None:
            name = uuid4().hex

        if name in self._names:
            raise Exception()

        self._data[name] = data
        self._index[len(self._data)] = name
        self._names.add(name)

    def get_layers(self):
        for name, data in self._data.items():
            yield name, data
