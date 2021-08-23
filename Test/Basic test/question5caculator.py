def add():
    num1=int(input("Enter the first number:"))
    num2 =int(input("Enter the second number:"))
    return num1+num2
def diff():
    num1=int(input("Enter the first number:"))
    num2 =int(input("Enter the second number:"))
    return num1-num2
def mul():
    num1=int(input("Enter the first number:"))
    num2 =int(input("Enter the second number:"))
    return num1*num2
def div():
    num1=int(input("Enter the first number:"))
    num2 =int(input("Enter the second number:"))
    return num1/num2
def floor():
    num1=int(input("Enter the first number:"))
    num2 =int(input("Enter the second number:"))
    return num1//num2
def exp():
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    return num1**num2
flag=True
while flag:
    choice=int(input("1.addition  2.Subtraction  3.multiplication  4.Division  5.Floor division   6.exponent 0.exit \n Enter your choice:"))
    if choice==1:
        print("The sum is:",add())
    elif choice==2:
        print("The difference is:",diff())
    elif choice == 3:
        print("The product is:", mul())
    elif choice == 4:
        print("The division result is:", div())
    elif choice == 5:
        print("The floor division result is:", floor())
    elif choice == 6:
        print("The exponent result is:", exp())
    else:
        flag=False

