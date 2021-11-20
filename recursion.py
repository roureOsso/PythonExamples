# -*- coding: utf-8 -*-

"""
DEFINITION: Recursion is a method of programming/coding a problem, in which a function calls itself one or more times.

A recursive function has to terminate. A recursive function terminates, if with every recursive call the solution of the
problem is downsized and moves towards a base case. A base case is a case, where the problem can be solved without
further recursion.  A recursion can end up in an infinite loop, if the base case is not met in the calls.

------------------------------------------------------------------------------------------------------------------------

Please try to give your best trying to solve this problems before checking the solutions. I you have though about a
task for a while and you are still not capable of solving the exercise maybe you could pair coding, it's fun!
(Or you could also sneakpeek the solutions)

Consider that some of these exercises could be solved using iterative approaches it could be a nice practice trying to
find both solutions:


1.
Write a factorial recursive Python function. This essentially means: the value in the n-th position is the result of
all the previous n numbers multiplied.
F(n) = F1 · F2 · ... · Fn-1 · n


2.
Write a recursive function that prints all the numbers of the fibonacci sequence the n integer.
The Fibonacci numbers are defined by (the addition of the two previous values):

Fn= Fn-1 + Fn-2


3.
Think of a recursive version of the function f(n) = 3 · n, i.e. the multiples of 3


4.
Write a recursive Python function that returns the sum of the first n integers.
(Hint: The function will be similiar to the factorial function!)


5.
Write a function which implements the Pascal's triangle:

                 1

              1    1

          1     2     1

       1     3     3     1

   1     4     6     4     1

1     5     10    10     5    1


6.
The Fibonacci numbers are hidden inside of Pascal's triangle.
If you sum up the coloured numbers of the following triangle, you will get the 7th Fibonacci number:

                         1

                      1    1

                  1     2     1

               1     3     3     |1|

           1     4     |6|     4     1

        1     |5|     10    10     5    1

     |1|     6     15    20    15    6    1

Write a recursive program to calculate the Fibonacci numbers, using Pascal's triangle.


7.
Implement a recursive function in Python for the sieve of Eratosthenes.

The sieve of Eratosthenes is a simple algorithm for finding all prime numbers up to a specified integer.
It was created by the ancient Greek mathematician Eratosthenes.
The algorithm to find all the prime numbers less than or equal to a given integer n:

- Create a list of integers from two to n: 2, 3, 4, ..., n
- Start with a counter i set to 2, i.e. the first prime number
- Starting from i+i, count up by i and remove those numbers from the list, i.e. 2i, 3i, 4*i, etc..
- Find the first number of the list following i. This is the next prime number.
- Set i to the number found in the previous step
- Repeat steps 3 and 4 until i is greater than n. (As an improvement: It's enough to go to the square root of n)
- All the numbers, which are still in the list, are prime numbers

You can easily see that we would be inefficient, if we strictly used this algorithm,
e.g. we will try to remove the multiples of 4, although they have been already removed by the multiples of 2.
So it's enough to produce the multiples of all the prime numbers up to the square root of n. We can recursively
create these sets.


8.
Write a recursive function fib_indexfib(), which returns the index of a number in the Fibonacci sequence,
if the number is an element of this sequence, and returns -1 if the number is not contained in it, i.e.
fib(fib_index(n)) == n

"""
import timeit
from functools import partial

"""
1.
"""


def factorial(n):
    if n <= 1:
        return n

    return n * factorial(n - 1)


# for l in range(10):
#     print(factorial(l))

"""
2.
"""


def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


# for l in range(10):
#     print(fibonacci(l))


"""
3.
"""


def mult3(n):
    if n <= 1:
        return n * 3

    return 3 + mult3(n - 1)


# for l in range(10):
#     print(mult3(l))

"""
4. 
"""


def sum_n_int(n):
    if n == 0:
        return 0

    return n + sum_n_int(n - 1)


# for l in range(10):
#     print(sum_n_int(l))

"""
5.
"""


def pascal_triangle(n):
    """
    This solution the values corresponding to the iterations.
    """
    if n == 1:
        return [1]

    else:
        preb_line = pascal_triangle(n - 1)
        line = [1]
        for i in range(len(preb_line) - 1):
            line.append(preb_line[i] + preb_line[i + 1])

        line.append(1)

        return line


# print(pascal_triangle(5))


def pascal_triangle_draw(n):
    """
    This solution uses a list comp and prints the entire Pascal's triange, this makes it slightly more complicated to
    read it, but not that much :)

    Notice that I'm using a nested function to keep track of the original count value so I'm able to create a prettier
    pyramid without asking the user to introduce two time the same value.
    """

    def _pascal_triangle_draw(k, orig_n):

        if k == 1:
            print("  " * (orig_n - 1) + "1")
            return [1]

        else:
            preb_line = _pascal_triangle_draw(k - 1, orig_n)
            line = [preb_line[i] + preb_line[i + 1] for i in range(len(preb_line) - 1)]
            line.insert(0, 1)
            line.append(1)

            line_str = "  " * (orig_n - k) + "  ".join([str(i) for i in line])

            print(line_str)
            return line

    _pascal_triangle_draw(n, n)


# pascal_triangle_draw(20)


"""
6.
"""


def fib_pascal(n):
    """
    Notice that `fib_pascal` is essentially a wrapper for `_fib_pascal_calc` so we don't need to have two different
    functions and the user doesn't need to take care of anything else that the asking for the desired fibonacci number.
    """

    def _fib_pascal_calc(k, fib_pos):
        """
        Here we are essentially doing the same operation done to create the Pascal's triangle, BUT when going "deep" we
        keep track of the recursion using `fib_pos` adding. Using `fib_pos` the number corresponding to the index is
        added to `fib_sum`.
        """
        if k == 0:
            line = []
            fib_sum = 0

        elif k == 1:
            line = [1]
            fib_sum = 1 if fib_pos == 0 else 0

        else:
            line = [1]
            previous_line, fib_sum = _fib_pascal_calc(k - 1, fib_pos + 1)
            for i in range(len(previous_line) - 1):
                line.append(previous_line[i] + previous_line[i + 1])

            line += [1]
            if fib_pos < len(line):
                fib_sum += line[fib_pos]

        return line, fib_sum

    return _fib_pascal_calc(n, 0)[1]


# for l in range(0, 10):
#     print(fib_pascal(l))


"""
7.
"""


def isieve(n):
    """
    This is the iterative solution for the problem which I think, shows better how this algorithms works.
    For this example I'm using a set because checking membership and removing elements is faster.
    """

    # Create a list with all the numbers from 2 up to n
    numbers = set(range(2, n + 1))

    for i in range(2, n + 1):
        # For each number if it's not `numbers` list (is a multiple of a previous one) jump to the next one
        if i not in numbers:
            continue

        # If the square of the number is bigger than n, we can stop the iteration
        if i ** 2 > n:
            break

        # For all the rest of the numbers we find all the multiples up to i * n and then remove them
        for ii in range(2, n + 1):
            if i * ii > n:
                continue
            elif i * ii in numbers:
                numbers.remove(i * ii)

        # Instead of removing them one by one we could create the union of all the sets and intersect the resulting
        # set with `numbers`

    return numbers


# print(isieve(10))


def rsieve(n):
    """
    This is the recursive solution for the problem. For this example I decided to use sets so I could group all the
    multiples together and then remove them from the `numbers` set at once. (This is not necessarily faster).
    """
    numbers = set(range(2, n + 1))

    def _sieve(k):
        multiples = {k * i for i in range(2, n + 1) if k * i <= n}

        if k == 2:
            return multiples

        return multiples.union(_sieve(k - 1))

    # notice that I use square n rather than n, this is the same check done for the iterative version
    return numbers.difference(_sieve(int(n ** 0.5)))


# print(rsieve(10))
# print("recursive approach: " + str(timeit.timeit(partial(rsieve, 100), number=1000)))
# print("iterative approach: " + str(timeit.timeit(partial(isieve, 100), number=1000)))


"""
8.
"""


def fibonacci_index(n):
    """
    Notice that for every iteration we are finding all the fib numbers up to a certain index, this is highly inefficient
    you can see how to solve this problem following the examples in `memoization.py`
    """
    i = 0
    fib_num = 0
    while fib_num <= n:
        fib_num = fibonacci(i)
        if fib_num == n:
            return i

        i += 1

    return -1

# for l in range(10):
#     print(fibonacci(l), end=" ")
#
# print("")
# print("___________")
# print(fibonacci_index(8))
# print(fibonacci_index(4))
