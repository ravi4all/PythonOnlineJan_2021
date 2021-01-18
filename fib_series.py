#Fibonacci Series - 0,1,1,2,3,5,8,13,21

a = 1
b = 0
c = 0

while b < 100:
    print(b)
    '''
    c = a + b
    a = b
    b = c
    '''
    a,b = b, a + b
