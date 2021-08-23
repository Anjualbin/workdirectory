# polymorphisam ... more than one form
# overloading ..... Python doesnot support overloading(same method name but different num of arguements.while calling based on the num of arguments given metho will work)
# overriding...... same method with same no of arguments in parent and child class. child class method will override on parent class method

class Operators:
    def num(self,n1):
        self.n1=n1
        print("Inside parent class:",self.n1)
class Display(Operators):
    def num(self,n3):
        self.n3=n3
        print("Inside child class:",self.n3)

#op=Operators()
#op.num(2,3)
d=Display()
d.num(3)
