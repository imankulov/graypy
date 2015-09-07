# -*- coding: utf-8 -*-
import pytest
from graypy.field_converters import flat, recurse


class T(object):
    def __repr__(self):
        return '<T>'


@pytest.mark.parametrize('value,converted', [
    ('foo', 'foo'),
    (1, 1),
    ([1, 2, 3], '[1, 2, 3]'),
    ({'a': 1}, "{'a': 1}"),
])
def test_flat_converter(value, converted):
    assert flat(value) == converted


@pytest.mark.parametrize('value,converted', [
    ('foo', 'foo'),
    (1, 1),
    ([1, 2, 3], [1, 2, 3]),
    ({'a': 1}, {'a': 1}),
    ({'a': [1, 2, 3, {'foo': 'bar'}]}, {'a': [1, 2, 3, {'foo': 'bar'}]}),
    ([T()], ['<T>']),
])
def test_recurse(value, converted):
    assert recurse(value) == converted
