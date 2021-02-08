import functools

output = functools.reduce(lambda x,y : x + y, [4,3,5,7,8])
print(output)