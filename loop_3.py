#Nested For Loops
'''
for i in range(5):
    for j in range(5):
        print(i,j)
    print('=' * 30)
'''

'''
*****
*****
*****
*****
*****
'''
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()
print('=' * 30)
'''
*
**
***
****
*****
'''
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()

print('=' * 30)

'''
*****
****
***
**
*
'''
for i in range(5):
    for j in range(5 - i):
        print('*', end='')
    print()

print('=' * 30)

'''
1
12
123
1234
12345
'''
for i in range(5):
    for j in range(0,i+1):
        print(j+1, end='')
    print()

print('=' * 30)

for i in range(5):
    for j in range(5 - i):
        print(' ', end='')
    for k in range(2 * i + 1):
        print('*', end='')
    print()




