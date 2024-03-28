from math import sqrt


def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess


def golden_update(guess):
    return 1 / guess + 1


def square_close_to_successor(guess):
    return appro_eq(guess * guess, guess + 1)


def appro_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

phi = 1/2+sqrt(5)/2

def improve_test():
    approx_phi = improve(golden_update,square_close_to_successor)
    assert appro_eq(phi,approx_phi), 'phi differs from its approximation'
    