class Book():
    def __init__(self, title, author, isbn, availability=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = availability

    def info(self):
        pass

class Borrower():
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_books = []

    def info(self):
        pass
        



class Library(Book, Borrower):
    def __init__(self):
        self.books = ["The Hitchhiker's Guide to the Galaxy", "Harry Potter", "The Hobbit", "Ready Player One"]
        self.borrower = [("John",1337)]

    def find_books(self):
        search = input("Search the book you are looking for: ")
        if search in self.books:
            #return f"'{search}' is available."
            return self
        else:
            return f"'{search}' is unavailable."

    def find_borrower(self):
        search = input("Search for User name: ")
        if search.lower() in self.borrower:
            return f"Welcome {self.borrower}."
        #else:
            #add_borrower() ### needs to be implemented 
    
    def loan_book(self):
        borrower = self.find_borrower()
        book = self.find_books()

        if book and borrower:
            book.availability = False
            borrower.borrowed_books.append(book)
            print(f"Succesfully loaned {book.title}")
        
        elif not borrower:
            print("Borrower not found")

        elif not book:
            print("Book not found")

        else:
            print("Book not available")

    def return_book(self, borrower_id, book_isbn):
        borrower = self.find_borrower(borrower_id)
        book = self.find_book(book_isbn)

        if book and borrower and book in borrower.borrowed_books:
            book.availability = True
            borrower.borrowed_books.remove(book)
            print(f"{book.title} has been returned by {borrower.name}")
        elif not borrower:
            print("Borrower not found")
        elif not book:
            print("Book not found")
        else:
            print("Book is already available")





b = Library()
print(b.loan_book())
print(b.find_books())