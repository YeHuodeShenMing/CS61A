def trace(fn):
    def wrapped(x):
        print(f"-> {fn} ({x})")
        return fn(x)

    return wrapped


def triple(x):
    return 3 * x


triple = trace(triple)
