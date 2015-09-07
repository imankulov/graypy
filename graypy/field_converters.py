# -*- coding: utf-8 -*-
import sys
PY3 = sys.version_info[0] == 3


if PY3:
    string_type = str
    integer_type = (int, )
else:
    string_type = basestring
    integer_type = (int, long)


def flat(value):
    """
    Flat and safe field converter.

    Populates log records with key: value or key: repr(value) records
    """
    if not isinstance(value, (string_type, float) + integer_type):
        value = repr(value)
    return value


def recurse(value):
    """
    Takes value and tries to extract as much structured JSON as it can
    """
    if isinstance(value, dict):
        return {str(k): recurse(v) for k, v in value.items()}
    if isinstance(value, (list, dict)):
        return [recurse(v) for v in value]
    return flat(value)
