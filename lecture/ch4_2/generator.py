def letters_generators():
    current = "a"
    while current <= "d":
        yield current
        current = chr(ord(current) + 1)

for letter in letters_generators():
    print(letter)
