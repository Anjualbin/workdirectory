#The __str__ method is useful for a string representation of the object,
# either when someone codes in str(your_object), or even when someone might do print(your_object).

class Employee:
    compnay="ABC"
    def __init__(self,name,id,salar,exp):
        self.name=name
        self.id=id
        self.salary=salar
        self.exp=exp
    def printval(self):
        print("Name:",self.name,"ID:",self.id)

    def __str__(self):
        return self.name+"  "+str(self.exp)

emp=Employee("Anju",1234,3.5,4)
print(emp)           # calls the object and then it will pass to __str__ method and returns the value from there