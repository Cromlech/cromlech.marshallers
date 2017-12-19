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
        binary = False
        
        @staticmethod
        def loads(string):
            return rapidjson.loads(string, object_hook=decode_custom)

        @staticmethod
        def dumps(struct):
            return rapidjson.dumps(struct, default=encode_custom)
    
        @staticmethod
        def load(fd):
            data = fd.read()
            return rapidjson.loads(data, object_hook=decode_custom)

        @staticmethod
        def dump(struct, fd):
            data = rapidjson.dumps(struct, default=encode_custom)
            fd.write(data)
