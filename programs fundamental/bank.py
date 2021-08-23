# bank program

fixed_deposit=10000.00

amount=float(input("Enter the amount to withdraw:"))
if amount>fixed_deposit:
    print("You dont have the sufficient balance")
else:
    balance=fixed_deposit-amount
    print("your balance is",balance)