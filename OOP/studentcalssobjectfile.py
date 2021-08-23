class Student:
    def __init__(self,name,id,course,mark):
        self.name=name
        self.id=id
        self.course=course
        self.mark=mark
    def info(self):
        print("Name:",self.name)
        print("ID:",self.id)
        print("Course:",self.course)
        print("Mark:",self.mark)

f1=open("Student","r")
for i in f1:
    lst=i.split(",")
    obj=Student(lst[0],lst[1],lst[2],lst[3])
    obj.info()