# -*- coding: utf-8 -*-

import json
import datetime
from .prototype import Marshaller


def decode_custom(obj):
    custom_type = obj.get('__custom__')
    if custom_type == 'datetime':
        obj = datetime.datetime.strptime(
            obj["payload"], "%Y%m%dT%H:%M:%S.%f")
    elif custom_type == 'date':
        obj = datetime.datetime.strptime(
            obj["payload"], "%Y%m%d").date()
    return obj


def encode_custom(obj):
    if isinstance(obj, datetime.datetime):
        return {'__custom__': 'datetime',
                'payload': obj.strftime("%Y%m%dT%H:%M:%S.%f")}
    if isinstance(obj, datetime.date):
        return {'__custom__': 'date',
                'payload': obj.strftime("%Y%m%d")}
    return obj


class JSONMarshaller(Marshaller):
    """Pretty basic JSON marshaller.
    It provides a way to encode and decode datetime/date objects.
    Create your own marshaller in order to customize more.
    """
    @staticmethod
    def loads(string):
        return json.loads(string, object_hook=decode_custom)

    @staticmethod
    def dumps(struct):
        return json.dumps(struct, default=encode_custom)

    @staticmethod
    def load(fd):
        return json.load(fd, object_hook=decode_custom)

    @staticmethod
    def dump(data, fd):
        json.dump(data, fd, default=encode_custom)
