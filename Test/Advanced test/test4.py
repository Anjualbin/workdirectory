class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("Name:",self.name)
        print("Age:",self.age)

class Employee(Person):
    def __init__(self,name,age,company,id,salary):
        super().__init__(name,age)
        self.company=company
        self.id=id
        self.sal=salary
    def printinfo(self):
        print("Company:",self.company)
        print("Emp id:",self.id)
        print("Salary",self.sal)

emp=Employee("Sneha",24,"TCS",456,"30K")
emp.info()
emp.printinfo()