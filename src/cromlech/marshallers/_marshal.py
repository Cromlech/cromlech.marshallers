# -*- coding: utf-8 -*-

import marshal
from .prototype import Marshaller


class MarshalMarshaller(Marshaller):
    """Very basic `marshal` marshaller.
    """
    @staticmethod
    def loads(string):
        return marshal.loads(string)

    @staticmethod
    def dumps(struct):
        return marshal.dumps(struct)

    @staticmethod
    def load(path):
        with open(path, 'r') as fd:
            return marshal.load(fd)

    @staticmethod
    def dump(data, path):
        with open(path, 'w') as fd:
            marshal.dump(data, fd)
