from tree import *


def make_path(t, p):
    # t for Tree, and p for Paths
    assert p[0] == label(t)
    if len(p) == 1:
        return t
    new_branches = []
    found_p1 = False
    for b in branchs(t):
        if label(b) == p[1]:
            new_branches.append(make_path(b, p[1:]))
            found_p1 = True
        else:
            new_branches.append(b)
    if not found_p1:
        new_branches.append(make_path(tree(p[1]), p[1:]))
    return tree(label(t), new_branches)


t = tree(3, [tree(4), tree(5, [tree(6), tree(7)])])
