class Student():
    schoolname="Bishop cotton girls school"
    def setval(self,name,rollno,mark):
        self.name=name
        self.no=rollno
        self.mark=mark
    def info(self):
        print("Name:",self.name)
        print("Roll no:",self.no)
        print("Score:",self.mark)
        print("School:",Student.schoolname)

st1=Student()
a=input("Enter the name of student:")
b=int(input("Enter the rollno:"))
c=int(input("Enter the score:"))
st1.setval(a,b,c)
st1.info()