def curried_pow(x):
    def h(y):
        return pow(x, y)

    return h


def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start += 1
