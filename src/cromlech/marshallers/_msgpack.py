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

        binary = True

        @staticmethod
        def loads(string):
            return msgpack.unpackb(
                string, object_hook=decode_custom, raw=False)

        @staticmethod
        def dumps(struct):
            return msgpack.packb(
                struct, default=encode_custom, use_bin_type=True)

        @staticmethod
        def load(fd):
            data = fd.read()
            return msgpack.unpackb(
                data, object_hook=decode_custom, raw=False)

        @staticmethod
        def dump(struct, fd):
            packed = msgpack.packb(
                struct, default=encode_custom, use_bin_type=True)
            fd.write(packed)
