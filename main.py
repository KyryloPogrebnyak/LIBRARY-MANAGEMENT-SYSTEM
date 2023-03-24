class Library:
    def __init__(self, books, borrower):
        self.books = books
        self.borrower = borrower

class Book(Library):
    def __init__(self, title, author, isbn, availability):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = availability

    def info()

class Borrower(Library):
    def __init__(self, name, id, borrowed_books):
        self.name = name
        self.id = id
        self.borrowed_books = borrowed_books

    def info()