def add():
    num1 = float(input("enter the first number1:"))
    num2 = float(input("enter the second number:"))
    print("The result is:",num1+num2)

def sub():
    num1 = float(input("enter the first number1:"))
    num2 = float(input("enter the second number:"))
    print("The result is:",num1-num2)

def mul():
    num1 = float(input("enter the first number1:"))
    num2 = float(input("enter the second number:"))
    print("The result is:",num1*num2)

def div():
    num1 = float(input("enter the first number1:"))
    num2 = float(input("enter the second number:"))
    print("The result is:",num1/num2)
a=False
print("Select operation:\n 1.addition \n 2.subtraction \n 3.multiplication \n 4.division \n 5.exit")
while not a:
    choice=int(input("enter your choice:"))
    if choice==1:
        add()
    elif choice==2:
        sub()
    elif choice==3:
        mul()
    elif choice==4:
        div()
    else:
        a=True