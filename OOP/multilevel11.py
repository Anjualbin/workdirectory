class Person:
    def setvalue(self,name,age):
        self.name=name
        self.age=age
class Perant(Person):
    def pvalue(self,address):
        self.add=address
        print(self.name,self.add)
class Employee(Perant):
    def evalue(self,id):
        self.id=id
        print(self.name,self.add,self.id)

pe=Perant()
pe.setvalue("Amal",30)
pe.pvalue("abc")

emp=Employee()
emp.setvalue("akhil",45)
emp.pvalue("ert")
emp.evalue(1234)