"""Generalization"""


def identity(k):
    return k


def cube(k):
    return pow(k, 3)


def summation(n, term):
    """
    >>> summation(5,cube)
    225
    >>> summation(4,identity)
    10
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


def sum_naturals(n):
    """
    >>> sum_naturals(10)
    55
    >>> sum_naturals(5)
    15
    """
    return summation(n, identity)
