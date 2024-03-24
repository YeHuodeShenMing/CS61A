negate = lambda f, x: -f(x)
ans = negate(lambda x: x + 1, 6)
print(ans)
