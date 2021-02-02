# variable length argument
def add(*x):
    # print(x)
    # print(sum(x))
    count = 0
    for i in x:
        count += i
    print("Sum is",count)

add(5)
add(4,5)
add(4,5,6,7)
add(2,3,54,6,78,8,5,3,3)
