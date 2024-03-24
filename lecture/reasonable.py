def reasonable(n):
    """"
    >>> reasonable(10**1000)
    False
    >>> reasonable(0)
    True
    """
    return n == 0 or (1 / n) != 0
