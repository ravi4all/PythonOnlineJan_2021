# def person(**details):
#     print(details)
#
# person(name = 'Ram', age = 40)
# person(name = 'Shyam', age = 45, sal = 45000)
# person(age = 45, dept = 'IT', name = 'Ram')

def person(*args, **kwargs):
    print(args)
    print(kwargs)

person(101,'Ram',dept = 'IT')