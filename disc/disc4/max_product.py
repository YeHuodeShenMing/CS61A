def max_product(s):
    """Return the maximum product of non-consecutive elements of s.

    >>> max_product([10, 3, 1, 9, 2])   # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5])  # 5 * 5 * 5
    125
    >>> max_product([])                 # The product of no numbers is 1
    1
    """
    if len(s) < 2:
        return 1
    else:
        return max_product(s[2:]) * s[0]
    # def product(i):
    #     if i == len(s) or i == len(s) + 1 :
    #         return 1
    #     else:
    #         return product(i + 2) * s[i]

    # # max([product(i) for i in range(len(s))])

    # return max([1] + [product(i) for i in range(len(s))])
