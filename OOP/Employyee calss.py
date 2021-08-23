class Employee:
    def setval(self,name,id,deptment,salary):
        self.name=name
        self.id=id
        self.dept=deptment
        self.sal=salary
    def info(self):
        print("Employee name:",self.name)
        print("Employee id:",self.id)
        print("Department:",self.dept)
        print("Salary:",self.sal)

emp1=Employee()
emp1.setval("Anu",56,"development","3.2lpa")
emp1.info()

emp2=Employee()
emp2.setval("Aaa",12,"Accounting","2.5lpa")
emp2.info()