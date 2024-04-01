def main():
    s = [10, 3, 1, 9, 2]
    print(product(0, s))


def product(i, s):
    if i == len(s) or i == len(s) + 1:
        return 1
    else:
        return product(i + 2, s) * s[i]


main()
