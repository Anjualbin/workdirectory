class Student:
    def __init__(self,name,id,course,mark):
        self.name=name
        self.mark=mark
        self.course=course
        self.id=id
    def printinfo(self):
        print(self.name,self.id,self.course,self.mark)


file=open("student","r")
c=0
mark=[]
lst1=[]
for i in file:
    lst=i.rstrip().split(",")
    obj=Student(lst[0],lst[1],lst[2],lst[3])
    lst1.append(obj)
for st in lst1:
    mark.append(st.mark)
print(mark)
for st in lst1:
    if (st.mark==max(mark)):
        print(st.name,st.mark,st.course,st.id)



