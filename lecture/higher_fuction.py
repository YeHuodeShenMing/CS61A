def make_adder(n):
    """输入一个参数K
        返回一个N+K
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """

    def adder(k):
        return k + n

    return adder
