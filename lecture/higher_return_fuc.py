def multiply_by(m):
    """
    >>> multiply_by(2)(3)
    6
    >>> times_three = multiply_by(3)
    >>> times_three(5)
    15
    """
    def multiply(n):
        return n * m

    return multiply
