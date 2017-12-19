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
        def load(path):
            with open(path, 'rb') as fd:
                data = yaml.load(data, stream=fd)
            return data

        @staticmethod
        def dump(struct, path):
            with open(path, 'wb') as fd:
                data = yaml.dump(struct, stream=fd)
