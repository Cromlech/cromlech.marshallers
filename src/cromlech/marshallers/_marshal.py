# -*- coding: utf-8 -*-

import marshal
from .prototype import Marshaller


class MarshalMarshaller(Marshaller):
    """Very basic `marshal` marshaller.
    """

    binary = True

    @staticmethod
    def loads(string):
        return marshal.loads(string)

    @staticmethod
    def dumps(struct):
        return marshal.dumps(struct)

    @staticmethod
    def load(fd):
        return marshal.load(fd)

    @staticmethod
    def dump(data, fd):
        marshal.dump(data, fd)
