class College:
    def setval(self,clgname,place,nodept):
        self.clgname=clgname
        self.place=place
        self.nodept=nodept
    def printinfo(self):
        print("College Name:",self.clgname)
        print("Place:",self.place)
        print("No of Departments:",self.nodept)

class Employee(College):
    def emp(self,name,id,job):
        self.name=name
        self.id=id
        self.job=job
        print("Employee Details are:",self.name,self.id,self.job)
class Teachers(Employee):
    def std(self,dept):
        self.dept=dept
        print("Department:",self.dept)

# Single Inheritance
print("Single inheritance")
emp1=Employee()
emp1.setval("VJEC","Kannur",7)
emp1.printinfo()
emp1.emp("Sneha",23,"Teacher")

# Multilevel Inheritance
print("Multilevel inheritance")
t1=Teachers()
t1.setval("Ajec","Thrissur",6)
t1.printinfo()
t1.emp("Anju","1234","Librarian")
t1.std("CSE")

class Department():
    def dept(self,dep):
        self.dep=dep
        print("Department:",self.dep)

class Student(College,Department):
    def info(self,name,id):
        self.name=name
        self.id=id
        print(self.name,self.id)

print("Multiple iheritance")
std1=Student()
std1.setval("Ajec","Thrissur",6)
std1.printinfo()
std1.dept("Cse")
std1.info("Akhil",17)

