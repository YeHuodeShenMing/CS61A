def count_down(k):
    if k > 0:
        yield k
        yield from count_down(k - 1)
    """
    yield from count_down(k - 1)
    等价于
    for x in count_down(k - 1):
        yield x
    """


def a_then_b(a, b):
    yield from a
    yield from b


def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s


def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])

print(list(substrings("tops")))

def gen_fib():
    n, add = 0, 1
    while True:
        yield n #跟 return 一样，返回值但是不结束函数
        n, add = n + add, n

(lambda t: [next(t) for _ in range(10)])(gen_fib())

lambda x: f(x) #表示一个匿名函数，输入参数x，return出f(x)

[fn(x) for x in range(10)]#列表表达式，对每个在range(10) 范围内的 x 进行fn(x)操作，并返回list
