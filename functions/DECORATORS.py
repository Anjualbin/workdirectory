# Adding extra features to a function
# can use a decorator for multiple functions

def check(func):        # Creating decorator function
    def wrapper(name,age):  # create a wrapper function, can give any name to function, should have same no of variable of the main function
        if age<18:
            print(name,"Not eligible")
        else:
            return func(name,age)
    return wrapper

@check
def vaccine(name,age):
    print(name,"Eligible for vaccination")

vaccine("Anu",19)

@check
def voter_list(name,age):
    print("Eligible for registration")

voter_list("Amal",13)
