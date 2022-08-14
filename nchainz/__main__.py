from nchainz import Chainz
# debug
if __name__ == "__main__":
    class Chained(metaclass=Chainz):
        def f(self):
            ...
        def g(self):
            return 4
        @staticmethod
        def h():
            print("test")
    print(Chained.h())
