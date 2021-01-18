#walrus operator
a = 12
b = 15

#print("Sum is",c := a + b)

#print(f"Sum of {a} and {b} is {(c := a + b)}")

print(f"""
1. Add is {(c := a + b)}
2. Sub is {(d := a - b)}
3. Div is {(e := a / b)}
4. Mul is {(f := a * b)}
""")
