# SINGLE Inheriatance     Inherting a child class from parent/base/super class

class Person:                           # Parent class
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):                 # Child class, derived class, subclass
    def setval(self,id,company):
        self.id=id
        self.company=company

    def info(self):
        print("Name",self.name)
        print("Age:",self.age)
        print("Id:",self.id)
        print("Company",self.company)

emp=Employee("Anu",25)
emp.setval(123,"ls")
emp.info()