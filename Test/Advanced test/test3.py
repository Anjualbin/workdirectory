class Book:
    def __init__(self,library_name,book_name,author,pages):
        self.lbname=library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages
    def info(self):
        print("Library:",self.lbname)
        print("Book:",self.book_name)
        print("Author:",self.author)
        print("No of Pages:",self.pages)

b1=Book("Akpc Memorial library","Alchemist","Paulo coelo",456)
b1.info()