# -*- coding: utf-8 -*-

from .interface import Marshaller
try:
    import cPickle as pickle    #  python 2.x
except ImportError:
    import pickle               #  python 3.x


class PickleMarshaller(Marshaller):

    @staticmethod
    def loads(string):
        return pickle.loads(string)

    @staticmethod
    def dumps(struct):
        return pickle.dumps(struct)
    
    @staticmethod
    def load(path):
        with open(path, 'rb') as fd:
            return pickle.load(fd)

    @staticmethod
    def dump(data, path):
        with open(path, 'wb') as fd:
            pickle.dump(data, fd)
