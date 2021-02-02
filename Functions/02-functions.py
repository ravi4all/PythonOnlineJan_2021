# Global Variables
x = 10
y = 20

def add():
    # Local Variables
    x = 5
    y = 5
    z = x + y
    print("Sum is",z)

def sub():
    z = x - y
    print("Sub is",z)

add()
sub()