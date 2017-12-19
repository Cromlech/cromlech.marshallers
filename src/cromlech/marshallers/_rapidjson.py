# -*- coding: utf-8 -*-

try:
    import rapidjson
except ImportError:
    # FIXME: debug log.
    pass
else:
    from .prototype import Marshaller
    from ._json import encode_custom, decode_custom


    class RapidJSONMarshaller(Marshaller):
        """Base JSON Marshaller using RapidJSON.
        It provides an out-of-the-box date/datetime encoder/decoder.
        """
        @staticmethod
        def loads(string):
            return rapidjson.loads(string, object_hook=decode_custom)

        @staticmethod
        def dumps(struct):
            return rapidjson.dumps(struct, default=encode_custom)
    
        @staticmethod
        def load(fd):
            return rapidjson.loads(data, fd, object_hook=decode_custom)

        @staticmethod
        def dump(struct, fd):
            rapidjson.dump(struct, fd, default=encode_custom)
