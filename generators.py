"""
Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.

PERFORMANCE: The performance improvement from the use of generators is the result of the lazy (on demand) generation of
values, which translates to lower memory usage. Furthermore, we do not need to wait until all the elements have been
generated before we start to use them. This is similar to the benefits provided by iterators, but the generator makes
building iterators easy.

This can be illustrated by comparing the range and xrange built-ins of Python 2.x.


"""
from copy import deepcopy


class PowTwo:
    """
    This is the boiler plate for a generator. Notice the we have __next__ and next. This is due to a py2/py3
    compatibility need. Py2 needs next() and Py3 needs __next__()
    """
    def __init__(self, n):
        self.n = 0
        self.max = n

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result


# for i in PowTwo(2):
#     print(i)

"""
Using classes to create our generators has some downsides:
- there is a lot of boilerplate
- the logic has to be expressed in a somewhat convoluted way

Python provides generator functions as a convenient shortcut to building iterators. Lets rewrite the above iterator as 
a generator function:
"""


def pow_two_gen(n):
    """
    Yield is a keyword in Python that is used to return from a function without destroying the states of its local
    variable and when the function is called, the execution starts from the last yield statement.
    Any function that contains a yield keyword is termed a generator. Hence, yield is what makes a generator.
    """
    print("this is executed only once")
    k = 0
    while k < n:
        yield 2 ** k
        k += 1


for i in pow_two_gen(5):
    print(i)

"""
The next function is a real case implementation for a generator
"""


def padding_enumerate(iterable, start=0):
    """
    Can be used as you would use `enumerate`, will return the value of

    Args:
        iterable:  a sequence, an iterator, or objects that supports iteration
        start (int): `padding_enumerate()` starts counting from this number. If start is omitted, 0 is taken as start.

    Yields:
        tuple: adds counter to an iterable and returns it.
    """
    # If a iterable was given as an argument, we would loose it when trying to count it's size
    iterable_copy = deepcopy(iterable)

    # The item could be an iter so len() method would fail
    iter_len = sum(1 for _ in iterable_copy)

    n_order = len(str(iter_len - 1 + start))
    padding = n_order if n_order > 2 else 2

    for i, elem in enumerate(iterable, start=start):
        yield str(i).zfill(padding), elem


# # Example 1
# for n, _ in padding_enumerate(range(10)):
#     print("joint" + n)
#
# print("-"*20)
#
# # Example 2
# for n, trn in padding_enumerate(["trn1", "trn2", "trn3", "trn4", "trn5"]):
#     print("joint" + n)
