from uuid import uuid4
from collections import defaultdict


class Laminated:
    def __init__(self):
        self._union_data = dict()
        self._names = []

        self._data = defaultdict(dict)

    def __getitem__(self, item):
        return self._union_data[item]

    def add_layer(self, data, name=None):
        if name is None:
            name = uuid4().hex

        if name in self._names:
            raise ValueError('Duplicate layers names')

        self._names.insert(0, name)
        self._union_data.update(data)

        for k, v in data.items():
            self._data[k][name] = v

    def get_layers_names(self):
        for name in self._names:
            yield name

    def get_layer_item(self, name, item):
        start_search = False

        for layer_name in self._names:
            if layer_name == name:
                start_search = True
            if not start_search:
                continue

            if layer_name in self._data[item]:
                return self._data[item][layer_name]
        else:
            raise KeyError('{!r} not in dict'.format(item))
