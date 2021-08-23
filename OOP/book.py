# TWO TYPES OF VARIABLES
# Static variable: related to class ... access using class name
# instance variable..... related to method ... access using self

class Book:
    category="Fiction"      #Static variable
    def setval(self,name,author,nopages):
        self.name=name
        self.author=author
        self.pages=nopages
    def printinfo(self):
        print("Book name:",self.name)
        print("author:",self.author)
        print("category:",Book.category)        # printing static variable
        print("No of pages:",self.pages)

book1=Book()
book1.setval("Shages of twilight","Linda Howard",456)
book1.printinfo()

book2=Book()
book2.setval("Alchemist","paolo coehlo",560)
book2.printinfo()
