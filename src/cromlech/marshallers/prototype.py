# -*- coding: utf-8 -*-

import functools


class Marshaller(object):
    """Marshaller prototype.
    """

    @staticmethod
    def load(string):
        raise NotImplementedError

    @staticmethod
    def loads(fd):
        raise NotImplementedError

    @staticmethod
    def dump(struct):
        raise NotImplementedError

    @staticmethod
    def dumps(struct, fd):
        raise NotImplementedError

    def wraps(self, func):
        @functools.wraps(func)
        def marshalled_wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return self.dumps(result)
        return marshalled_wrapper

    @classmethod
    def load_from(cls, path):
        with open(path, 'r') as fd:
            return cls.load(fd)

    @classmethod
    def dump_to(cls, data, path):
        with open(path, 'w') as fd:
            cls.dump(data, fd)
