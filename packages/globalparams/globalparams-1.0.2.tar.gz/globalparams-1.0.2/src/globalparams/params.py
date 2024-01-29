
import json
from distutils.util import strtobool
from functools import reduce  # forward compatibility for Python 3
import operator

# source: https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
import sys


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Params(dict, metaclass=Singleton):
    def __init__(self, json_file=sys.argv[1]):
        super(Params, self).__init__()
        self.read(json_file)

    def read(self, fn):
        self.clear()
        self.update(json.load(open(fn, 'r')))

    def write(self, fn):
        json.dump(self, open(fn, 'w'), indent=4, sort_keys=True)

    def parse_args(self, set_vals=None):
        if set_vals is None:
            set_vals = sys.argv[1:]
        if len(set_vals) % 2 != 0:
            print(f"odd number of arguments")
            return
        set_vals = {set_vals[i]: set_vals[i + 1] for i in range(0, len(set_vals), 2)}
        for k, v in set_vals.items():
            k_ = k.split('/')
            try:
                last_node = reduce(operator.getitem, k_[:-1], self)
                if(type(last_node[k_[-1]])==bool):
                    v = strtobool(v)
                v_converted = type(last_node[k_[-1]])(v)
                last_node[k_[-1]] = v_converted
            except Exception as _:
                print(f"could not set key {k}")