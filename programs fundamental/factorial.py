num=int(input("enter the number to find factorial:"))
if a>0:
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print("The factorial is:",fact)
elif a==0:
    print("factorial of 0 is 1:")
else:
    print("please enter a positive number:")