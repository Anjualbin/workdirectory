# # to find the factorial of a number
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
#
#
# num = int(input("Enter the number to find factorial:"))
# print("The factorial of", num, "is", fact(num))


a=10 #global variable variable that is common in a program , it can be used inside the function as well

def add():
    #n=5    # local variable.  variable created inside the function.we cannot access this variable outside this function
    #print(n)
    print(a)
add()
print(a)














