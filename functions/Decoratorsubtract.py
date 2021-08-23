def check(func):
    def wrapper(num1,num2):
        if num1<num2:
            (num1,num2)=(num2,num1)
            return func(num1,num2)
        else:
            return func(num1,num2)

    return wrapper

@check
def subtract(num1,num2):
    print("The result is:",num1-num2)

subtract(5,10)

@check
def div(num1,num2):
    print("The division result is:",num1/num2)

div(3,15)