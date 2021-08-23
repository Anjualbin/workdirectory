class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("Nmae:",self.name,"age:",self.age)

class Student(Person):
    def __init__(self,rollno,mark,name,age):
        super().__init__(name,age)
        self.rollno=rollno
        self.mark=mark
    def print(self):
        print("Rollno:",self.rollno)
        print("Mark",self.mark)

st=Student(12,45,"Anju",23)
st.printval()
st.print()
