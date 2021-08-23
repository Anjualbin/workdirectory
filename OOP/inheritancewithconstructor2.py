class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("Name:",self.name,"Age:",self.age)

class Employee(Person):
    def __init__(self,empid,sal,name,age):
        super().__init__(name,age)
        self.empid=empid
        self.sal=sal
    def print(self):
        print("Empid:",self.empid)
        print("Salary",self.sal)

emp=Employee(1234,25000,"an",23)
emp.printval()
emp.print()