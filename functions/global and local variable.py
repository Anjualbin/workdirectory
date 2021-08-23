# def printval():
#     x=5    # local variable cannot be used outside the function
#     global y # global variable can be accessed outside the function as well
#     y=6
#     print(x)
#     print(y)
# printval()
# print(y)
# print(x)    # will get an error over here


def even(num):

    if num%2==0:
        print("even")
    else:
        print("odd")


a=int(input("Enter the number:"))
even(a)                             # passing argument while calling the function.






