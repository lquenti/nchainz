# nchainz - Automatic Method Chaining in Python
A metaclass for automatic method chaining. (Only for methods that return `None`, obviously)

```python
from nchainz import Chainz

class A(metaclass=Chainz):

  def has_return_value(self):
    return 4

  def this_is_chainable(self):
    print("hello")
    # implicitly returns self

a = A()
assert a = a.this_is_chainable().this_is_chainable()
assert a.has_return_value() == 4
```


## What is Method Chaining?

[Method chaining](https://en.wikipedia.org/wiki/Method_chaining) describes the Syntax of not having to assign objects
between methods which are changing the state.

For example, in JS one can just chain the array transformations like

```JS
[1,2,3,4,5,6].filter(x => x % 2 == 0).map(x => x * x).find(x => x > 30)
```

## How to do it manually?

Pretty easy. You just return `self`. Here is an example:

```python
class MyNum:
  def __init__(self, x):
    self.x = x
  def inc(self):
    self.x += 1
    return self

three = MyNum(3)
six = three.inc().inc().inc()
assert three.x+3 == six.x
```

## Install

```
pip install nchainz
```

## Use

Just use the `Chainz` metaclass:

```python
from nchainz import Chainz

class MyClass(metaclass=Chainz):
  ...
```

## Why? Like seriously, Why?

I had my 5 minutes, I am sorry.

## Further reading

It's such a great read, you should really read it. (Written for Python 2)

[Meta-classes Made Easy](https://web.archive.org/web/20200124090402id_/http://www.voidspace.org.uk/python/articles/metaclasses.shtml)
