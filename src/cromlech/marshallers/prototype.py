# -*- coding: utf-8 -*-

import functools
import portalocker


class Marshaller(object):
    """Marshaller prototype.
    """

    binary = False
    
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

    @classmethod
    def load_from(cls, path, timeout=5):
        mode = cls.binary and 'rb' or 'r'
        try:
            with portalocker.Lock(path, mode=mode, timeout=timeout) as fd:
                data = cls.load(fd)
        except portalocker.exceptions.LockException:
            raise OSError('Resource is busy and could not be freed.')
        return data

    @classmethod
    def dump_to(cls, data, path, timeout=5):
        mode = cls.binary and 'wb' or 'w'
        try:
            with portalocker.Lock(path, mode=mode, timeout=timeout) as fd:
                cls.dump(data, fd)
        except portalocker.exceptions.LockException:
            raise OSError('Resource is busy and could not be freed.')

    def wraps(self, func):
        @functools.wraps(func)
        def marshalled_wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return self.dumps(result)
        return marshalled_wrapper
