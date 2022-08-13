# TODO: Support py2 with tox

from functools import wraps
from types import FunctionType

def chainz(f):
    @wraps(f)
    def wrap(self, *args, **kwargs):
        res = f(self, *args, **kwargs)
        return self if res is None else res
    return wrap

# https://web.archive.org/web/20200124090402id_/http://www.voidspace.org.uk/python/articles/metaclasses.shtml#a-method-decorating-metaclass
def MetaClassFactory(f):
    class MetaClass(type):
        def __new__(cls, class_name, bases, class_dict):
            new_class_dict = {}
            for name, attr in class_dict.items():
                new_class_dict[name] = f(attr) if isinstance(attr, FunctionType) else attr
            print(f"{new_class_dict=}")
            return type.__new__(cls, class_name, bases, new_class_dict)
    return MetaClass

Chainz = MetaClassFactory(chainz)

if __name__ == "__main__":
    class A(metaclass=Chainz):
        def f(self, a,b):
            print(a+b)
        def g(self, a, b):
            return a+b
        def __str__(self):
            return "haha"
    print(A().f(5,6).f(6,6).g(1,1))
