class Person:
    def setval(self,name,age):
        self.name=name
        self.age=age
    def printinfo(self):
        print("name:",self.name)
        print("age:",self.age)

person1=Person()
person1.setval("anu",24)
person1.printinfo()