from tree import *

t2 = tree(5, [tree(6), tree(7)])
t1 = tree(3, [tree(4), t2])
result = label(min(branchs(max([t1, t2], key=label)), key=label))

"""
branchs(max([t1, t2], key=label) = [tree(6), tree(7)]
6
"""