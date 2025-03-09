
class Library :
    def __init__(self) :
        self.books = [
            Book("The Silent Storm"),
            Book("Echoes of the Past"),
            Book("Whispers in the Dark"),
            Book("The Crimson Throne"),
            Book("Shadows of Tomorrow"),
            Book("The Forgotten Path"),
            Book("Frozen in Time"),
            Book("Secrets of the Lost"),
            Book("Golden Horizons"),
            Book("The Last Chronicle")
        ]
        self.members = []
    def add_book(self, book_name) :
        self.books.append(Book(book_name))
    def add_member(self, name) :
        self.members.append(Member(name))


class Book():
    def __init__(self,title) :
        self.title = title
        self.is_borrowed = False
        
    def borrow(self) :
            self.is_borrowed  = True
    def return_book(self) :
            self.is_borrowed = False

class Member() :
    def __init__(self, name) :
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book) :
           
        if book.is_borrowed : 
             print("This book is borrowed.")
             return
        if len(self.borrowed_books) >= 3 :
             print("You can't borrow a book")
             return

        self.borrowed_books.append(book)
        book.borrow()
            
               

    def return_book(self, book) :
        if book not in self.borrowed_books :
             print("you did not borrow this book")
             return
        self.borrowed_books.remove(book)
        book.return_book()
        
               

            


             




        

        
        
