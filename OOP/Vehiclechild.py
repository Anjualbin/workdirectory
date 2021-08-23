class Vehicle:
    def __init__(self,company,color,model):
        self.company=company
        self.color=color
        self.model=model
    def info(self):
        print("Company:",self.company)
        print("Color:",self.color)
        print("Model:",self.model)

class Bus(Vehicle):
    def __init__(self,num,company,color,model):
        super().__init__(company,color,model)
        self.num=num

obj=Bus(123,"Toyota","White","T400")
obj.info()


