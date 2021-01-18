# by defualt python input function return string type of data
f_name = input("Enter your first name : ")
l_name = input("Enter your last name : ")
name = f_name + " " + l_name
print("Hello " + name)

# so we need to perform type casting/conversion
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
#res = a + b
#print(res)

c = a + b
d = a - b
e = a / b
f = a * b
print(f"""
    Sum is {c = }
    Sub is {d = }
    Div is {e = }
    Mul is {f = }
""")
