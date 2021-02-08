def even(num):
    return num % 2 == 0

def odd(num):
    return num % 2 != 0

# e = even(6)
# print(e)
numbers = [4,4,6,7,8,9,3,34,5,8,9]
# even_num = []
# odd_num = []
# for i in range(len(numbers)):
#     if even(numbers[i]):
#         even_num.append(numbers[i])
#     else:
#         odd_num.append(numbers[i])

# print(even_num)
# print(odd_num)

e = list(filter(even, numbers))
print(e)

o = list(filter(odd, numbers))
print(o)



