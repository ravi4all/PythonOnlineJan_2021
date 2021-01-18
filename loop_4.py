'''
hint - use chr()
a
ab
abc
abcd
abcde
'''
for i in range(5):
    for j in range(i+1):
        print(chr(97+j), end='')
    print()

'''
hint : using 3rd variable
1
23
456
78910
'''
k = 1
for i in range(4):
    for j in range(0,i+1):
        print(k, end='')
        k = k + 1
    print()

print('*' * 20)

'''
    1
   2 3
  4 5 6
 7 8 9 10
'''
n = 1
for i in range(4):
    for k in range(4 - i):
        print(' ', end='')
    for j in range(0,i+1):
        print(n, end=' ')
        n = n + 1
    print()










