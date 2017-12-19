# -*- coding: utf-8 -*-

import pickle
from .prototype import Marshaller


class PickleMarshaller(Marshaller):

    binary = True

    @staticmethod
    def loads(string):
        return pickle.loads(string)

    @staticmethod
    def dumps(struct):
        return pickle.dumps(struct)
    
    @staticmethod
    def load(fd):
        return pickle.load(fd)

    @staticmethod
    def dump(data, fd):
        pickle.dump(data, fd)
