try:
    x = int(input("Enter a number : "))
    y = int(input("Enter a number : "))

    add = x + y
    sub = x - y
    div = x / y
    mul = x * y

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid Input, Enter a digit")

except BaseException as err:
    print("Some error",err)

else:
    print("Sum is", add)
    print("Sub is", sub)
    print("Div is", div)
    print("Mul is", mul)