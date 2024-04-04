empty = "empty"


def is_link(s):
    return s == empty or (len(s) == 2 and is_link(s[1]))


def link(first, rest):
    assert is_link(rest)
    return [first, rest]


def first(s):
    assert is_link(s)
    assert s != empty
    return s[0]


def rest(s):
    assert is_link(s)
    assert s != empty
    return s[1]


four = link(1, link(2, link(3, link(4, empty))))


def len_link(s):
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length


def getitem_link(s, i):
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)


def extend_link(s, t):
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))


def apply_to_all_link(f, s):
    assert is_link(s)
    if s == empty:
        return s
    return link(f(first(s)), apply_to_all_link(f, rest(s)))


t = apply_to_all_link(lambda x: x * x, four)


def keep_if_link(f, s):
    # Return the element is s if f(s) equals to True
    assert is_link(s)
    if s == empty:
        return s
    else:
        kept = keep_if_link(f, rest(s))
        if f(first(s)):
            return link(first(s), kept)
        else:
            return kept


k = keep_if_link(lambda x: x % 2 == 0, four)


def join_link(s, separator):
    if s == empty:
        return s
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)


j = join_link(four, ", ")
