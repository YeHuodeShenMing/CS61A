def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"

    def check_all(i):
        if i == n:
            return True
        elif n % i == 0:
            return False
        else:
            return check_all(i + 1)

    return check_all(2)
