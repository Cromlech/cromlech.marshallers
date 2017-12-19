# -*- coding: utf-8 -*-

try:
    import yaml
except ImportError:
    # FIXME: debug log.
    pass
else:
    from .prototype import Marshaller


    class YAMLMarshaller(Marshaller):

        @staticmethod
        def loads(string):
            return yaml.load(string)

        @staticmethod
        def dumps(struct):
            return yaml.dump(struct)

        @staticmethod
        def load(fd):
            return yaml.load(stream=fd)

        @staticmethod
        def dump(struct, fd):
            yaml.dump(struct, stream=fd)
