from operator import add, mul, truediv


def divide_all(n, ds):
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')


def reduce(f, s, initial):
    """
    >>> reduce(mul, [2,4,6,8], 1)
    64
    >>> reduce(add, [1,2,3,4], 0)
    10
    """
    if not s:
        return initial
    else:
        first, rest = s[0], s[1:]
        return reduce(f, rest, f(initial, first))