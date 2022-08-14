import pytest

from nchainz import Chainz


class Unchained:
    def f(self):
        ...


class Chained(metaclass=Chainz):
    def f(self):
        ...

    def g(self):
        return 4

    @staticmethod
    def h():
        ...


def test_unchained_fails():
    with pytest.raises(AttributeError):
        Unchained().f().f()


def test_chained_works():
    c = Chained()
    assert c is c.f().f().f().f()


def test_staticmethod_is_ignored():
    assert Chained.h() is None


def test_returning_functions_are_ignored():
    assert Chained().f().f().f().g() == 4
