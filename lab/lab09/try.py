def composed(f, g):
    def inner(x):
        return f(g(x))

    return inner


# Example usage:
def add_one(x):
    return x + 1


def square(x):
    return x * x


add_one_then_square = composed(square, add_one)


# Now, add_one_then_square behaves as square(add_one(x))
# print(add_one_then_square(5))  

def repeat(f, n):
    if n == 1:
        return f
    else:
        return composed(f, repeat(f, n - 1))


def gcd(a, b):
    small = min(a, b)
    big = max(a, b)
    if big % small:
        big = big % small
    for i in range(small,1,-1):
        if big % i == 0 and small % i == 0:
            return i
    return 1
print(gcd(4,24))