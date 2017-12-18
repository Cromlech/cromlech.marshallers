# -*- coding: utf-8 -*-

try:
    import msgpack
except ImportError:
    # FIXME: debug log.
    pass
else:
    from .interface import Marshaller
    from .cm_json import encode_custom, decode_custom


    class MsgpackMarshaller(object):
        """Base Marshaller using msgpack.
        It provides an out-of-the-box date/datetime encoder/decoder.
        """
        @staticmethod
        def loads(string):
            return msgpack.unpackb(string, object_hook=decode_custom)

        @staticmethod
        def dumps(struct):
            return msgpack.packb(struct, default=encode_custom)
    
        @staticmethod
        def load(path):
            with open(path, 'rb') as fd:
                data = fd.read()
            return msgpack.unpackb(data, object_hook=decode_custom)

        @staticmethod
        def dump(struct, path):
            packed = msgpack.packb(struct, default=encode_custom)
            with open(path, 'wb') as fd:
                fd.write(packed)
