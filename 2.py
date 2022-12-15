#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import timeit


class TailRecurseException:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs

def tail_call_optimized(g):
    def func(*args, **kwargs):
        f = sys._getframe()
    if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
        raise TailRecurseException(args, kwargs)
    else:
        while True:
            try:
                return g(*args, **kwargs)
            except TailRecurseException, e:
                args = e.args
                kwargs = e.kwargs

    func.__doc__ = g.__doc__
    return func


def fib(i, current = 0, next = 1):
    if i == 0:
        return current
    else:
        return fib(i - 1, next, current + next)


def factorial(n, acc=1):
    if n == 0:
        return acc
    return factorial(n-1, n*acc)


@tail_call_optimized
def factorial_opt(n, acc=1):
    if n == 0:
        return acc
    return factorial(n-1, n*acc)


@tail_call_optimized
def fib(i, current = 0, next = 1):
    if i == 0:
        return current
    else:
        return fib(i - 1, next, current + next)


if __name__ == '__main__':
    print("Time for factorial with stack introspection: ")
    print(f'{timeit.timeit(lambda: factorial_opt(10000), number=10000)}\n')
    print("Time for factorial w/o stack introspection: ")
    print(timeit.timeit(lambda: factorial(10000), number=10000))
    print("Time for factorial with stack introspection: ")
    print(f'{timeit.timeit(lambda: fib_opt(10000), number=10000)}\n')
    print("Time for factorial w/o stack introspection: ")
    print(timeit.timeit(lambda: fib(10000), number=10000))