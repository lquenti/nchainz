from functools import wraps
from types import FunctionType


def chainz(f):
    @wraps(f)
    def wrap(self, *args, **kwargs):
        res = f(self, *args, **kwargs)
        return self if res is None else res

    return wrap


def metaclass_factory(f):
    class MetaClass(type):
        def __new__(cls, class_name, bases, class_dict):
            new_class_dict = {}
            for name, attr in class_dict.items():
                new_class_dict[name] = f(attr) if isinstance(attr, FunctionType) else attr
            return type.__new__(cls, class_name, bases, new_class_dict)

    return MetaClass


Chainz = metaclass_factory(chainz)
