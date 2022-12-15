#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
from functools import lru_cache


def factorial(n):
    product = 1
    while n > 1:
        product *= n
    n -= 1
    return product


def factorial_rec(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial_rec(n - 1)


def fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


def fib_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n - 2) + fib_rec(n - 1)


@lru_cache()
def factorial_lru(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial_lru(n - 1)


@lru_cache()
def fib_lru(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_lru(n - 2) + fib_lru(n - 1)


if __name__ == '__main__':
    print("Time for iterative version of factorial: ")
    print(timeit.timeit(lambda: factorial(22), number=10000))
    print("Time for recurse version of factorial: ")
    print(timeit.timeit(lambda: factorial_rec(22), number=10000))
    print("Time for recurse with lru version of factorial: ")
    print(timeit.timeit(lambda: factorial_lru(22), number=10000))

    print("\nTime for iterative version of fib: ")
    print(timeit.timeit(lambda: fib(22), number=10000))
    print("Time for recurse version of fib: ")
    print(timeit.timeit(lambda: fib_rec(22), number=10000))
    print("Time for recurse with lru version of fib: ")
    print(timeit.timeit(lambda: fib_lru(22), number=10000))