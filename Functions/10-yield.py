def counter():
    x = 0
    while True:
        x += 1
        yield x

count = counter()
# print(next(count))
for i in count:
    print(i)
    if i == 10:
        break
