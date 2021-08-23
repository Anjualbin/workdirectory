class Bank:
    def setval(self,name,accountno):
        self.name=name
        self.accountno=accountno
        self.balance=5000
    def withdraw(self):
        c=int(input ("enter the amount to withdraw:"))
        if c<self.balance:
            self.balance=self.balance-c
            print("amount withdraw done: your current balance is:",self.balance)
    def deposit(self):
        a=int(input("Enter the amount to deposit:"))
        self.balance=self.balance+a
        print("Your balance is:",self.balance)

custom1=Bank()
custom1.setval("anju",12345)
custom1.deposit()
custom1.withdraw()

