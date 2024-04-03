def max_product(s):
    """Return the maximum product of non-consecutive elements of s.

    >>> max_product([10, 3, 1, 9, 2])   # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5])  # 5 * 5 * 5
    125
    >>> max_product([])                 # The product of no numbers is 1
    1
    >>> max_product([10, 3, 1, 9, 2, 7, 8])
    720
    """
    if len(s)==0:
        return 1
    return max(max_product(s[2:])*s[0],max_product(s[1:]))
max_product([10, 3, 1, 9, 2])
    # if len(s) == 0:
    #     return 1
    # elif len(s) == 1:
    #     return s[0]
    # elif len == 2:
    #     return max(s[0], s[1])
    # else:
    #     return max(max_product(s[:-1]), max_product(s[:-2]) * s[len(s) - 1])
