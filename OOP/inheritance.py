#INHERITANCE .. inherits the properties of one class by onother

class Person:
    def stval(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    def setvalue(self,dept,mark):
        self.dept=dept
        self.mark=mark
    def info(self):
        print("Name:",self.name)             #Inheriting the value from person class
        print("Department",self.dept)
        print("Mark:",self.mark)


st=Student()
st.stval("Anu",21)
st.setvalue("CSE",1150)
st.info()