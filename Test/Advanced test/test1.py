class Vehicle:
    def setval(self,Company,Color,Number):
        self.company=Company
        self.color=Color
        self.num=Number
    def printval(self):
        print("Company:",self.company)
        print("Color:",self.color)
        print("Number:",self.num)

class Car(Vehicle):
    def info(self,Model):
        self.model=Model
        print("Model:",self.model)


obj= Car()
obj.setval("Toyota","White","TMP1234")
obj.printval()
obj.info("Fortuner")
