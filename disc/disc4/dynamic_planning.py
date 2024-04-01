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
    dp = [[0 for _ in range(n)] for _ in range(m)]
    # 初始化二维数组
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] == 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]
