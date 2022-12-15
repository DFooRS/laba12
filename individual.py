#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_numbers(a):
    if len(a) == 1:
        return [a]

    temp = []

    for i in a:
        new_a = [x for x in a if x != i]
        z = print_numbers(new_a)

        for t in z:
            temp.append([i] + t)

    a = temp
    return a


if __name__ == '__main__':
    n = int(input("Enter n: "))
    a = [i + 1 for i in range(n)]
    for j in print_numbers(a):
        print(j)