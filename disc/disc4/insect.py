def main():
    paths(2, 2)
    print(res)


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    global res
    res = 0

    def move(x, y):
        global res
        if x < m and y < n:
            return move(x + 1, y) or move(x, y + 1)
        elif x == m and y != n:
            return move(x, y + 1)
        elif x != m and y == n:
            return move(x + 1, y)
        elif x == m and y == n:
            res += 1
            return
        # else:
        #     pass

    move(1, 1)
    return res


main()
