# bi, bj, pi, pj = map(int, input().split())
# while bi >= 0 and bj >= 0 and pi >= 0 and pj >= 0:
#     for i in range(bi):
#         for j in range(bj):
#             if i == pi and  j == pj:


#     bi, bj, pi, pj = map(int, input().split())
def f(a, b):
    sum = 1
    div = 1
    for i in range(a + b, b, -1):
        sum *= i
    for i in range(1, a+1):
        div *= i
    return sum / div


m, n, o, p = map(int, input().split(","))
while m >= 0 and n >= 0 and o >= 0 and p >= 0:

    if o <= m and p <= n:
        res = f(m, n)
        dec = f(o, p) * f(m - o, n - p)
        print (int(res - dec))
    else:
        res = f(m, n)
        print (int(res))
    m, n, o, p = map(int, input().split(","))
