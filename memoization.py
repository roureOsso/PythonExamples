"""
DEFINITION: Memoization is a technique used in computing to speed up programs. This is accomplished by memorizing the
calculation results of processed inputs such as the results of function calls. This results would be accessed if the
same process with the same inputs was to be executed, avoiding unnecessary calculation.
In many cases a simple array is used for storing the results, but lots of other structures can be used as well.

------------------------------------------------------------------------------------------------------------------------

- This file will make usage of `decorators` if you are unfamiliar go check: decorators.py

- For the following examples I will be using the The  fibonacci recursive function that you can find here: recursion.py
Go check it if you have any doubt

------------------------------------------------------------------------------------------------------------------------

The fibonacci recursive implementation is highly inefficient. Finding the fifth fib number implies the addition of the
fourth and third number, at the same time, the fourth will imply the second and third and so on (recursively). As you
can see we are repeating operations. Memoizing this function would reduce the time complexity because we would be
reducing to 1 the number of times a position is calculated.
"""

from functools import wraps, partial
import timeit


def fibonacci(n):
    """
    This is the original function, it will be used to compare execution times.
    """
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def wrap_fib(n):
    """
    For this first solution I'm wrapping the actual fibonacci function. Each time `_fib` gets executed the value is
    stored in `memo` so the next time the same value is asked there is no need for calculating it again.

    Notice that I could have solved this is several different ways, it's not really necessary to wrap `_fib` and `memo`
    under the same function. Either way the problems would be similar:
        - The actual fib function needs to me modified to work with `memo`.
        - Another function needs to be called.
    """
    memo = {}

    def _fib(k):
        if k not in memo:
            if k <= 1:
                memo[k] = k
            else:
                memo[k] = _fib(k - 1) + _fib(k - 2)

        return memo[k]

    return _fib(n)


# print("non memoized: " + str(timeit.timeit(partial(fibonacci, 37), number=1)))
# print("memoized: " + str(timeit.timeit(partial(wrap_fib, 35), number=1)))

def memoize(f):
    """
    This solution is way cleaner, this is what we already know as a decorator. This is essentially taking a function,
    passing it as `f`. Notice how `_fib` and `wrap` are doing the same check with `memo`, the only difference is that
    `wrap` instead of implementing the task will simply call the actually fib function.
    """
    memo = {}

    def wrap(*n):
        if n[0] not in memo:
            memo[n[0]] = f(*n)

        return memo[n[0]]

    return wrap


"""In order to make this work we need to pass `fibonacci` to `memoize` and reassign `fibonacci` again so it actually
points to `wrap` and the memo system is taken into account. 
`memo[n] = f(n)` will execute the "original" fibonacci function, if this one calls to it self (fibonacci) will actually
call `wrap` and so on... 

See decorators for more details.
"""

# fibonacci = memoize(fibonacci)
#
# print("memoized as a decoration: " + str(timeit.timeit(partial(fibonacci, 37), number=1)))
# print("memoized: " + str(timeit.timeit(partial(wrap_fib, 35), number=1)))


@memoize
def fib(n, a):
    """
    Of course the cleanest solution is to use a Python Decorator so the used doesn't need to decorate nothing on its own
    """
    print(a)
    if n <= 1:
        return n
    else:
        return fib(n - 1, a) + fib(n - 2, a)


"""This three solutions are basically the same when it comes to evaluation time."""

# print("memoized: " + str(timeit.timeit(partial(wrap_fib, 35), number=1)))
# fibonacci = memoize(fibonacci)
# print("memoized as a decoration: " + str(timeit.timeit(partial(fibonacci, 37), number=1)))
# print("memoized with decorator: " + str(timeit.timeit(partial(fib, 37), number=1)))

