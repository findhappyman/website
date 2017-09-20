a = iter(range(5))

while True:
    try:
        print(next(a))
    except StopIteration:
        break
