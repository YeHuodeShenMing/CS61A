def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)

        return h

    return g


def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start += 1


def uncurry2(g):
    def f(x, y):
        return g(x)(y)

    return f
