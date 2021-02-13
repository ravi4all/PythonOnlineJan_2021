def atm():
    total = 10000
    pin = input("Enter your PIN : ")
    if pin == "1234":
        print("Login Success")
    else:
        # print("Login Failed")
        raise ValueError("Login Failed")

    amt = int(input("Enter the amount : "))
    if amt < total:
        total -= amt
        print("Remaining balance is",total)
    else:
        raise ValueError("Insufficient Balance")

try:
    atm()
except ValueError as err:
    print(err)
    atm()
