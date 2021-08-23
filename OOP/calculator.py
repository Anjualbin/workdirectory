class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print("The sum is:",self.num1+self.num2)
    def diif(self):
        print("The difference is :", self.num1-self.num2)
    def div(self):
        print("The division result is:",self.num1/self.num2)
    def mul(self):
        print("The product is:",self.num1*self.num2)

calc1=Calculator(12,23)
calc1.add()
calc1.diif()
calc1.div()
calc1.mul()