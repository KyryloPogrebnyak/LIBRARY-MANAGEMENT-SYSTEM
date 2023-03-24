class Book():
    def __init__(self, title, author, isbn, availability):
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
        self.borrower = []

    def find_books(self):
        search = input("Search the book you are looking for: ")
        if search in self.books:
            return f"'{search}' is available."
        else:
            return f"'{search}' is unavailable."

    def find_borrower(self):
        search = input("Search for User name: ")
        if search.lower() in self.borrower.lower():
            return f"Welcome {self.borrower}."
        else:
            add_borrower() ### needs to be implemented 

b = Library()
print(b.find_books())