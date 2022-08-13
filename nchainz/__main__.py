from nchainz import Chainz
# debug
if __name__ == "__main__":
    class A(metaclass=Chainz):
        def f(self, a,b):
            print(a+b)
        def g(self, a, b):
            return a+b
        def __str__(self):
            return "haha"
    print(A().f(5,6).f(6,6).g(1,1))
