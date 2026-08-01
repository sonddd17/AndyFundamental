class library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
       if title not in self.books:
           self.books.append(title)
       else:
           print("book is already lib") 

    def list_books(self):
        print(self.books)

    def remove_book(self,title):
        if title in self.books:
            self.books.remove(title)
        else:
            print("Book is not available")
    


my_lib = library()

my_lib.add_book("Nha Gia Kim")
my_lib.add_book("Nha Gia Kim")   # duplicate - should NOT be added twice
my_lib.list_books()

my_lib.remove_book("Nha Gia Kim")
my_lib.list_books()

my_lib.remove_book("A Book That Doesn't Exist")   # should print the "not available" message