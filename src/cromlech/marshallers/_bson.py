# -*- coding: utf-8 -*-

try:
    import bson
except ImportError:
    # FIXME: debug log.
    pass
else:
    from .prototype import Marshaller

    
    class BSONMarshaller(Marshaller):

        @staticmethod
        def loads(string):
            return bson.loads(string)

        @staticmethod
        def dumps(struct):
            return bson.dumps(struct)

        @staticmethod
        def load(path):
            with open(path, 'rb') as fd:
                data = fd.read()
            return bson.loads(data)

        @staticmethod
        def dump(struct, path):
            data = bson.dumps(struct)
            with open(path, 'wb') as fd:
                fd.write(data)
