class Vscode:
    def compile(self):
        print("Compiling from Vscode")
    def debug(self):
        print("Debugging from Vscode")
    def execute(self):
        print("Executinging from Vscode")

class Pycharm:
    def compile(self):
        print("Compiling from pycharm")
    def debug(self):
        print("Debugging from pycharm")
    def execute(self):
        print("Executinging from pycharm")

class Programmer:
    def coding(self,obj):
        obj.compile()
        obj.debug()
        obj.execute()

p=Pycharm() # create a object for class Pycharm
dev=Programmer()   # create object for programmer class
dev.coding(p)   # calling the function inside Programmer class with reference as Pycharm class object

