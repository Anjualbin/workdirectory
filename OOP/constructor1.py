# constructor to intialize instance variables
# constructor automatically invoke when object creates

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("Name:",self.name)
        print("Age:",self.age)

person1=Person("Abc",25)
person1.info()
