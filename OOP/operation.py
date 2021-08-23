class Operation():
    def setval(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def result(self):
        print("The rasult is:",self.num1+self.num2)

add=Operation()
add.setval(5,3)
add.result()