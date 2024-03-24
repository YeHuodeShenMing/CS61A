from operator import mul


def square(x):
    return mul(x, x)


def make_adder(n):
    def adder(k):
        return k + n

    return adder


def scale(f, x, k):
    """
    >>> scale(square,3,2)
    18
    >>> scale(make_adder(3),3,2)
    12
    >>> scale(square,2,5)
    20
    >>> scale(lambda x: x * 3 + 1, 7, 4)
    88
    """
    return k * f(x)



