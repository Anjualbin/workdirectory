class Employee:
    def salary(self,hour):
        self.hour=hour
        print("Salry:",250*self.hour)

class Parttime(Employee):
    def salary(self,hour):
        self.hour=hour
        print("Salary:",150*self.hour)

p=Parttime()
p.salary(10)