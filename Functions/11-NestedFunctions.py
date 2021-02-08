# def outer():
#     def inner():
#         pass

def calc():
    x = 5
    y = 7
    def add():
        z = x + y
        return z
    def sub():
        z = x - y
        return z
    return add, sub

# add = calc()
# print(add())

operations = calc()
print(operations[0]())
print(operations[1]())
