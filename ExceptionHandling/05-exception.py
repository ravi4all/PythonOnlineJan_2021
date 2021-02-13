def atm():
    total = 10000
    pin = input("Enter your PIN : ")
    assert (pin == "1234"), "Login Failed"
    print("Login Success")
    amt = int(input("Enter the amount : "))

    assert (amt < total), "Insufficient Balance"
    total -= amt
    print("Remaining balance is",total)

try:
    atm()
except AssertionError as err:
    print(err)
    atm()
