# -*- coding: utf-8 -*-

try:
    import bson
except ImportError:
    # FIXME: debug log.
    pass
else:
    from .prototype import Marshaller

    
    class BSONMarshaller(Marshaller):

        binary = True

        @staticmethod
        def loads(string):
            return bson.loads(string)

        @staticmethod
        def dumps(struct):
            return bson.dumps(struct)

        @staticmethod
        def load(fd):
            data = fd.read()
            return bson.loads(data)

        @staticmethod
        def dump(struct, fd):
            data = bson.dumps(struct)
            fd.write(data)
