a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = a + b
d = a - b
e = a / b
f = a * b
print(c)
print("Sum is %d"%c)
print("Sum of %d and %d is %d"%(a,b,c))

print("Sum is",c)
print("Sum of",a,"and",b,"is",c)

print("Sum is {}".format(c))
print("Sum of {} and {} is {}".format(a,b,c))

#f-strings - fast strings
print(f"Sum of {a} and {b} is {c}")

#print("1. Add\n2. Sub\n3. Div")
#Multi line print
print(f"""
1. Add is {c}
2. Sub is {d}
3. Div is {e}
4. Mul is {f}
""")












