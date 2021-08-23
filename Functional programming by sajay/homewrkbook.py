class Book:
    books={"alchemist":{"book_name":"alchemist","author":"paulo","price":350,"copies":100,"sold":10},
           "halfgirlfriend": {"book_name": "halfgirlfriend", "author": "chetan", "price": 200, "copies": 200, "sold": 100},
           "rainrising": {"book_name": "rainraising", "author": "nirupama", "price": 100, "copies": 0, "sold": 50}
           }

    def find_book(self,bookname):
        if bookname in self.books:
            return bookname
            #print(bookname,"is available",self.books[bookname])
        else:
            return 0
            #print("The book you are searching is not available")

    def find_copies(self,bookname):
        if bookname in self.books:
            print(self.books[bookname]["copies"])

    def sort(self):
        res=sorted(self.books.items(),key=lambda x:x[1]["sold"], reverse=True)
        for i in res:
            print(i[1]["author"])

obj=Book()
bk=obj.find_book("alchemis")
obj.sort()
if bk==0:
    print("The book you are searching is not available")

else:
    obj.find_copies(bk)


