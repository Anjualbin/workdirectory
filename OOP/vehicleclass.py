class Vehicle():
    def __init__(self,model,color,price):
        self.model=model
        self.color=color
        self.price=price
    def print(self):
        print("Model:",self.model,"Color:",self.color,"Price",self.price)

    def __str__(self):           #method is the string representation of object,to work when we call print(objec)
        return self.model+str(self.price)       # return takes only one value, and --str method return only striong so conactenation applied

car=Vehicle("Xuv","Black","10l")
car.print()
print(car)