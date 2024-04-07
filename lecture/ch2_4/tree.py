def tree(root_label, branchs=[]):
    for branch in branchs:
        assert is_tree(branch)
    return [root_label] + list(branchs)


def label(tree):
    return tree[0]


def branchs(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False

    for branch in branchs(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branchs(tree)


t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])


"fibonacci Tree Recursive"


def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])


"count leaves"


def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branchs_count = [count_leaves(b) for b in branchs(tree)]
        return sum(branchs_count)


def partition_tree(n, m):
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n - m, m)
        right = partition_tree(n, m - 1)
        return tree(m, [left, right])


def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if label(tree):
            print(" + ".join(partition))
    else:
        left, right = branchs(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)


# def right_binarize(tree):
#     if is_leaf(tree):
#         return tree
#     if len(tree) > 2:
#         tree = [tree[0], tree[1:]]
#     return [right_binarize(b) for b in tree]
# def right_binarize(init_tree):
#     """Construct a right-branching binary tree."""
#     if is_leaf(init_tree):
#         return init_tree
#     if len(init_tree) > 2:
#         init_tree = [init_tree[0], init_tree[1:]]
#     return [right_binarize(b) for b in init_tree]


# [1,[2,[3,[4,[5,[6,7]]]]]]


def leaves(tree):
    "Return a list containing the leaf labels of tree"
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branchs(tree)], [])


l = leaves(fib_tree(5))


def count_paths(t, total):
    """
    >>> t = tree(3, [tree(-1), tree(1, [tree(2, [tree(1)]), tree(3)]), tree(1, [tree(-1)])])
    >>> count_paths(t, 3)
    2
    >>> count_paths(t, 4)
    2
    >>> count_paths(t, 5)
    0
    >>> count_paths(t, 6)
    1
    >>> count_paths(t, 7)
    2
    """
    if label(t) == total:
        found = 1
    else:
        found = 0
    return found + sum([count_paths(b, total - label(t)) for b in branchs(t)])
