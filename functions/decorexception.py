def admnrequire(func):
    def wrapper(user,no):
        if user!="admin":
            raise Exception("You dont have the permission")
        else:
            return func(user,no)
    return wrapper

@admnrequire
def changepin(user,pin):
    mypin=pin
    return mypin
@admnrequire
def deleteacnt(user,accno):
    return str(accno)+"deleted"
print(changepin("admin",678))
print(deleteacnt("user",12345))
