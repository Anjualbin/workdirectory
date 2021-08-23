class Animal:
    def __init__(self,category,nolegs,food):
        self.category=category
        self.nolegs=nolegs
        self.food=food
class Dog(Animal):
    def __init__(self,name,category,nolegs,food):
        super().__init__(category,nolegs,food)
        self.name=name
    def info(self):
        print(self.name,self.category,self.nolegs,self.food)

obj=Dog("Puppy","Dog",4,"Meat")
obj.info()
