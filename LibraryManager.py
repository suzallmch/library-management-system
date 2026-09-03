# ==========================================
# IMPORTS
# ==========================================
from datetime import date, timedelta
# 'date' lets us get today's date
# 'timedelta' lets us add/subtract days from a date


# ==========================================
# CLASS DEFINITIONS (the blueprints)
# ==========================================

class Book:
    def __init__(self, title, author, shelf_location):
        self.title = title
        self.author = author
        self.shelf_location = shelf_location
        self.is_available = True
        self.due_date = None   # no due date until the book is actually borrowed


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Student(Member):
    def __init__(self, name):
        super().__init__(name)
        self.borrow_limit = 3  # students can borrow up to 3 books


class Faculty(Member):
    def __init__(self, name):
        super().__init__(name)
        self.borrow_limit = 10  # faculty can borrow up to 10 books


class Guest(Member):
    def __init__(self, name):
        super().__init__(name)
        self.borrow_limit = 1  # guests can borrow only 1 book

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    # add a new book to the library
    def add_book(self, title, author, shelf_location):
        new_book = Book(title, author, shelf_location)
        self.books.append(new_book)

    # add a new member to the library
    def register_member(self, name, member_type):
        if member_type == "student":
            new_member = Student(name)
        elif member_type == "faculty":
            new_member = Faculty(name)
        elif member_type == "guest":
            new_member = Guest(name)
        else:
            print("Invalid member type.")
            return

        self.members.append(new_member)

    # borrow a book from the library
    def borrow_book(self, member, title):
        if len(member.borrowed_books) >= member.borrow_limit:
          print(f"{member.name} has reached their borrow limit.")
          return False
    
        for book in self.books:
            if book.title == title and book.is_available:
                book.is_available = False
                book.due_date = date.today() + timedelta(days=14)  # due 14 days from today
                member.borrowed_books.append(book)
                print(f"{member.name} borrowed '{title}', due back on {book.due_date}.")
                return True
        print(f"Book '{title}' is not available for borrowing.")
        return False

    # a member returns a book to the library
    def return_book(self, member, title):
        for book in member.borrowed_books:
            if book.title == title:
                # check if it's overdue BEFORE we clear the due_date
                if date.today() > book.due_date:
                    days_late = (date.today() - book.due_date).days
                    print(f"'{title}' was returned {days_late} day(s) late.")
                else:
                    print(f"'{title}' was returned on time.")

                book.is_available = True
                book.due_date = None   # clear the due date, it's back on the shelf
                member.borrowed_books.remove(book)
                return True
        print(f"Book '{title}' was not borrowed by {member.name}.")
        return False

    # check if a book is available in the library
    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_available:
                    print(f"Book '{title}' is available in the '{book.shelf_location}' in the library.")
                else:
                    print(f"Book '{title}' is not available in the library. Due back {book.due_date}.")
                return
        print(f"Book '{title}' is not found in the library.")


# ==========================================
# DATA (raw values used to create objects)
# ==========================================
book_data = [
    ("Dune", "Frank Herbert", "Sci-Fi A1"),
    ("1984", "George Orwell", "Dystopian B2"),
    ("Brave New World", "Aldous Huxley", "Dystopian B3"),
    ("The Hobbit", "J.R.R. Tolkien", "Fantasy C1"),
    ("Fahrenheit 451", "Ray Bradbury", "Dystopian B4"),
    ("The Great Gatsby", "F. Scott Fitzgerald", "Classics D1"),
    ("Animal Farm", "George Orwell", "Dystopian B5"),
    ("Moby Dick", "Herman Melville", "Classics D2"),
    ("War and Peace", "Leo Tolstoy", "Classics D3"),
    ("Crime and Punishment", "Fyodor Dostoevsky", "Classics D4"),
    ("The Catcher in the Rye", "J.D. Salinger", "Classics D5"),
    ("To Kill a Mockingbird", "Harper Lee", "Classics D6"),
    ("Pride and Prejudice", "Jane Austen", "Classics D7"),
    ("The Odyssey", "Homer", "Classics D8"),
    ("Frankenstein", "Mary Shelley", "Horror E1"),
    ("Dracula", "Bram Stoker", "Horror E2"),
    ("The Picture of Dorian Gray", "Oscar Wilde", "Classics D9"),
    ("Slaughterhouse-Five", "Kurt Vonnegut", "Sci-Fi A2"),
    ("The Alchemist", "Paulo Coelho", "Fiction F1"),
    ("Neuromancer", "William Gibson", "Sci-Fi A3"),
]

member_data = [
    ("Alice", "student"),
    ("Bob", "faculty"),
    ("Charlie", "guest"),
    ("Diana", "student"),
    ("Ethan", "faculty"),
]


# ==========================================
# SETUP PHASE (build the world — create real
# objects from the blueprints + data above)
# ==========================================

library = Library()

for title, author, shelf_location in book_data:
    library.add_book(title, author, shelf_location)

members = {}
for name, member_type in member_data:
    library.register_member(name, member_type)
    members[name] = library.members[-1]

