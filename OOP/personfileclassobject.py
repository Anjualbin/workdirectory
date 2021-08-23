class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("Name:",self.name)
        print("Age:",self.age)

f1=open("person","r")
for i in f1:
    lst=i.split(" ")
    obj=Person(lst[0],lst[1])
    obj.info()

# f1=open("person","r")
# for i in f1:
#     lst=i.rstrip("\n ").split(" ")
#     obj=Person(lst[0],lst[1])
#     obj.info()

