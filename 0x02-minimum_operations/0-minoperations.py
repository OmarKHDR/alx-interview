#!/usr/bin/env python3
""" creating a program for basic algebra"""
import math


def get_primes(n, arr):
    """as the name says"""
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            arr.append(i)
            get_primes(int(n / i), arr)
            break
    else:
        arr.append(n)


def minOperations(n):
    """how does it work?
    using some math it shows that sum of prime factors
    how to get prim factors?
    its numbers less than sqrt of n and are primes and mult to n
    """
    if n <= 1 or int(n) != n:
        return 0
    arr = []
    get_primes(n, arr)
    return sum(arr)
