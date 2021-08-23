age=int(input("Enter your age:"))

if age<18:
    raise Exception("Not eligible for vaccination")
else:
    print("Continue reg process for vaccination")