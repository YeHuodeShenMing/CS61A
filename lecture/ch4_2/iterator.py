# primes = [2, 3, 5, 7]
# iterator = iter(primes)
# try:
#     next(iterator)
# except StopIteration:
#     print("No more values")

# r = range(3, 13)
# s = iter(r)

# d = {"one": 1, "two": 2, "three": 3}


def double_and_print(x):
    print(f"*** {x} => {2*x} ***")
    return 2 * x


def is_even(x):
    print(f"{x} is an even")
    return x % 2 == 0 and x


s = range(3, 7)
doubled = map(double_and_print, s)
even = filter(is_even, s)
