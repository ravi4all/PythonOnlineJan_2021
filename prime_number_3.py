min_range = int(input("Enter min range : "))
max_range = int(input("Enter max range : "))

for num in range(min_range, max_range):
    for i in range(2,num):
        if num % i == 0:
            #print("Not Prime Number")
            break
    else:
        print("{} is Prime Number".format(num))
