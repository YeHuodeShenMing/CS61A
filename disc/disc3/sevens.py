def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(14, 5)
    5
    >>> sevens(16, 5)
    2
    >>> sevens(18, 5)
    2
    >>> sevens(20, 5)
    5
    """

    def f(i, who, direction):
        if i == n:
            return who
        "*** YOUR CODE HERE ***"
        if has_seven(i) or i % 7 == 0:
            direction = 0 - direction
        who = (who + direction) % k
        if who == 0:
            who += 5

        return f(i + 1, who, direction)

    return f(1, 1, 1)
    "As we can see, direction=1 represent for clockwise"


def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)


sevens(9, 5)
