def num(x):
    ans = 0
    dic = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    if x == 0:
        return dic[0]
    while x:
        ans += dic[x % 10]
        x //= 10
    return ans


# while True:
n = int(input())
count = 0
for i in range(1000 + 1):
    for j in range(0, 1000 + 1):
        k = i + j
        if num(i) + num(j) + num(k) == n - 4:
            count += 1
print(count)
