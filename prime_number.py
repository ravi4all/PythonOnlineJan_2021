num = 17
prime = True
for i in range(2,num):
    if num % i == 0:
        prime = False
        #print("Not Prime Number")
        break
    else:
        prime = True
        #print("Prime Number")


if prime:
    print("Prime Number")
else:
    print("Not Prime Number")
