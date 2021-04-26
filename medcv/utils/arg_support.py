# !/usr/bin/env python
# -*- coding:utf-8 -*-

import functools
from inspect import signature


def expected_type(*type_args, **type_kwargs):
    def decorator(fn):
        @functools.wraps(fn)
        def checker(*args, **kwargs):
            fn_signature = signature(fn)
            input_value = fn_signature.bind(*args, **kwargs).arguments
            require_type = fn_signature.bind_partial(*type_args, **type_kwargs).arguments
            for name, value in input_value.items():
                if name in require_type and not isinstance(value, require_type[name]):
                    raise TypeError('%s must be %s, but got %s' % (name, require_type[name], type(value)))
            return fn(*args, **kwargs)
        return checker
    return decorator


