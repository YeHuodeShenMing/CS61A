def find_digit(k):
    """Returns a function that returns the kth digit of x.

    >>> find_digit(2)(3456)
    5
    >>> find_digit(2)(5678)
    7
    >>> find_digit(1)(10)
    0
    >>> find_digit(4)(789)
    0
    """
    assert k > 0
    "*** YOUR CODE HERE ***"
    return lambda x: (x // pow(10, k - 1) % 10)
    # def func(x):
    #     i = 0
    #     while x and i<k:
    #         if i == k - 1:
    #             ans = x % 10
    #         x //= 10
    #         i += 1
    #     if len(str(x)) < k:
    #         ans = 0
    #     return ans

    # return func
