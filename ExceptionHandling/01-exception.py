try:
    x = int(input("Enter a number : "))
    y = int(input("Enter a number : "))

    add = x + y
    print("Sum is", add)

    sub = x - y
    print("Sub is", sub)

    div = x / y
    print("Div is", div)

    mul = x * y
    print("Mul is", mul)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid Input, Enter a digit")

except BaseException as err:
    print("Some error",err)