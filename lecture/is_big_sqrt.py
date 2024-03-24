from math import sqrt


def is_big_sqrt(x):
    """
    >>> is_big_sqrt(1000)
    True
    >>> is_big_sqrt(-1000)
    False
    """
    return x > 0 and sqrt(x) > 10


# 这里一定要注意，x>0和sqrt()在and的左右顺序也有讲究
# x>0放在右边，运行-1000就会报错
