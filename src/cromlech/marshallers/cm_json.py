# -*- coding: utf-8 -*-

import json
import datetime
from .interface import Marshaller


def decode_custom(obj):
    custom_type = date.get('__custom__')
    if custom_type == 'datetime':
        obj = datetime.datetime.strptime(
            obj["as_str"], "%Y%m%dT%H:%M:%S.%f")
    elif custom_type == 'date':
        obj = datetime.datetime.strptime(
            obj["as_str"], "%Y%m%d").date()
    return obj


def encode_custom(obj):
    if isinstance(obj, datetime.datetime):
        return {'__custom__': 'datetime',
                'as_str': obj.strftime("%Y%m%dT%H:%M:%S.%f")}
    if isinstance(obj, datetime.date):
        return {'__custom__': 'date',
                'as_str': obj.strftime("%Y%m%d")}
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
    def load(path):
        with open(path, 'r') as fd:
            return json.load(fd, object_hook=decode_custom)

    @staticmethod
    def dump(data, path):
        with open(path, 'w') as fd:
            json.dump(data, fd, default=encode_custom)
