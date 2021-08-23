# user can create Exception
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
if num1==num2:
    raise Exception("Two numbers are same:")
else:
    print(num1+num2)
