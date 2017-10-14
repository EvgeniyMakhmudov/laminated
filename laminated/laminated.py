from uuid import uuid4
from collections import OrderedDict


class Laminated:
    def __init__(self):
        self._data = OrderedDict()
        self._index = OrderedDict()
        self._union_data = dict()
        self._names = set()

    def __getitem__(self, item):
        return self._union_data[item]

    def add_layer(self, data, name=None):
        if name is None:
            name = uuid4().hex

        if name in self._names:
            raise Exception()

        self._data[name] = data
        self._index[len(self._data)] = name
        self._names.add(name)
        self._union_data.update(data)

    def get_layers_names(self):
        for name in self._data.keys():
            yield name

    def get_layer_item(self, name, item):
        return self._data[name][item]
