# -*- coding: utf-8 -*-

import functools
from zope.interface import Interface, provider


class IMarshaller(Interface):
    """Definition of a data marshaller.
    """

    def load(string):
        """Document me.
        """
    
    def loads(fd):
        """Document me.
        """

    def dump(struct):
        """Document me.
        """
    
    def dumps(struct, fd):
        """Document me.
        """

    def wraps(func):
        """Document me.
        """


@provider(IMarshaller)
class Marshaller(object):

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
