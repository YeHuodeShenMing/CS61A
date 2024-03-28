def square(x):
    return x * x


def sum_naturals(n):
    # total, k = 0, 1
    # while k <= n:
    #     total, k = total + k, k + 1
    # return total
    return summation(n, identity)


def identity(n):
    return n


def sum_cube(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + pow(k, 3), k + 1
    return total


def pi_sum(n):
    # total, k = 0, 1
    # while k <= n:
    #     total, k = total + 8 / ((4 * k - 3) * (4 * k - 1)), k + 1
    # return total
    return summation(n, pi_term)


def pi_term(x):
    return 8 / ((4 * x - 3) * (4 * x - 1))


def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total
