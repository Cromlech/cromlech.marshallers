# -*- coding: utf-8 -*-

try:
    import msgpack
except ImportError:
    # FIXME: debug log.
    pass
else:
    from .prototype import Marshaller
    from ._json import encode_custom, decode_custom


    class MsgpackMarshaller(Marshaller):
        """Base Marshaller using msgpack.
        It provides an out-of-the-box date/datetime encoder/decoder.
        """
        @staticmethod
        def loads(string):
            return msgpack.unpackb(
                string, object_hook=decode_custom, encoding='utf-8')

        @staticmethod
        def dumps(struct):
            return msgpack.packb(
                struct, default=encode_custom, use_bin_type=True)
    
        @staticmethod
        def load(path):
            with open(path, 'rb') as fd:
                data = fd.read()
            return msgpack.unpackb(
                data, object_hook=decode_custom, encoding='utf-8')

        @staticmethod
        def dump(struct, path):
            packed = msgpack.packb(
                struct, default=encode_custom, use_bin_type=True)
            with open(path, 'wb') as fd:
                fd.write(packed)
