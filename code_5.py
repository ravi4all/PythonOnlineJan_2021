# walrus operator - :=

print("Hello",name := input("Enter your name : "))

a = 5
b = 5

#c = a + b
#print("Sum is",c := a + b)

#print(f"Sum of {a} and {b} is {(c := a + b)}")

print(f"""
    Sum of {a} and {b} is {(c := a + b)}
    Sub of {a} and {b} is {(c := a - b)}
    Div of {a} and {b} is {(c := a / b)}
    Mul of {a} and {b} is {(c := a * b)}
""")
