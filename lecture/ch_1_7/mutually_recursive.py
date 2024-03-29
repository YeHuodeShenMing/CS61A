# def is_even(n):
#     if n == 0:
#         return True
#     else:
#         return is_odd(n - 1)


def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n - 1)


def is_even(n):
    if n == 0:
        return True
    else:
        if n - 1 == 0:
            return False
        else:
            return is_even((n - 1) - 1)


# result = is_even(4)


def play_alice(n):
    if n == 0:
        print("Bob wins!")

    else:
        play_bob(n - 1)


def play_bob(n):
    if n == 0:
        print("Alice wins!")
    else:
        if is_even(n):
            return play_alice(n - 2)
        else:
            return play_alice(n - 1)
