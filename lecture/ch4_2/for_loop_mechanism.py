counts = [1, 2, 3]
items = counts.__iter__()
try:
    while True:
        item = items.__next__()
        print(item)
except StopIteration:
    pass
