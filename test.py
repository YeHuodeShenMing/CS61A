# def factorial(n, i):  # n 为代求数字 ， i为变化量
#     if n == 1:
#         return 1
#     if i == 1:
#         return 0
#     ans = factorial(n, i - 1)
#     if n % i == 0:
#         ans += factorial(n // i, i)
#     return ans


# a = int(input())
# print(factorial(a, a))

m = int(input())


def partation(m, n):  # m apples, n plates, k is the biggest count for one plate.
    if m == 0:
        return 1
    if n == 1:
        return 1
    partation(m, n - 1)
    if m % n:
        return partation(m // n, n)


print(partation(m, m))
