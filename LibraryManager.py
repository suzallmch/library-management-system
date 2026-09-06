# ==========================================
# IMPORTS
# ==========================================
from datetime import date, timedelta
import itertools


# Generates 1, 2, 3, ... whenever a new Book is created.
# Each physical copy receives its own unique ID.
book_id_counter = itertools.count(1)


# ==========================================
# CLASS DEFINITIONS
# ==========================================
class Book:
    def __init__(self, title, author, shelf_location):
        self.book_id = next(book_id_counter)  # Unique ID, e.g. 1, 2, 3
        self.title = title
        self.author = author
        self.shelf_location = shelf_location
        self.is_available = True              # New books begin on the shelf
        self.due_date = None                  # No due date until borrowed


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []              # Stores Book objects borrowed by this member


class Student(Member):
    def __init__(self, name):
        super().__init__(name)
        self.borrow_limit = 3                 # Students can borrow up to 3 books


class Faculty(Member):
    def __init__(self, name):
        super().__init__(name)
        self.borrow_limit = 10                # Faculty can borrow up to 10 books


class Guest(Member):
    def __init__(self, name):
        super().__init__(name)
        self.borrow_limit = 1                 # Guests can borrow only 1 book


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    # Add a new physical book copy to the library.
    def add_book(self, title, author, shelf_location):
        new_book = Book(title, author, shelf_location)
        self.books.append(new_book)
        print(f"Added '{title}' with book ID {new_book.book_id}.")
        return new_book                   # Returning it can be useful later in the program

    # Register a member and assign the correct borrowing limit.
    def register_member(self, name, member_type):
        member_type = member_type.lower()  # Allows values such as "Student" or "STUDENT"

        if member_type == "student":
            new_member = Student(name)
        elif member_type == "faculty":
            new_member = Faculty(name)
        elif member_type == "guest":
            new_member = Guest(name)
        else:
            print("Invalid member type. Choose student, faculty, or guest.")
            return None

        self.members.append(new_member)
        print(f"Registered {name} as a {member_type}.")
        return new_member

    # Display every book and its ID so the user knows which ID to borrow.
    def list_books(self):
        if not self.books:
            print("There are no books in the library.")
            return

        print("\n--- Library Books ---")
        for book in self.books:
            status = "Available" if book.is_available else f"Borrowed (due {book.due_date})"
            print(
                f"ID: {book.book_id} | Title: {book.title} | "
                f"Author: {book.author} | Shelf: {book.shelf_location} | Status: {status}"
            )

    # Borrow a book by its ID instead of its title.
    # IDs allow the library to distinguish between multiple copies of one title.
    def borrow_book(self, member, book_id):
        if len(member.borrowed_books) >= member.borrow_limit:
            print(f"{member.name} has reached their borrow limit of {member.borrow_limit}.")
            return False

        for book in self.books:
            if book.book_id == book_id:
                if not book.is_available:
                    print(f"Book ID {book_id} ('{book.title}') is already borrowed.")
                    return False

                book.is_available = False
                book.due_date = date.today() + timedelta(days=14)  # Loans last 14 days
                member.borrowed_books.append(book)
                print(f"{member.name} borrowed '{book.title}', due back on {book.due_date}.")
                return True

        # This runs only if no matching ID was found in self.books.
        print(f"Book with ID {book_id} was not found.")
        return False

    # Return a book by its ID.
    def return_book(self, member, book_id):
        for book in member.borrowed_books:
            if book.book_id == book_id:
                # Check lateness before resetting due_date to None.
                if date.today() > book.due_date:
                    days_late = (date.today() - book.due_date).days
                    print(f"'{book.title}' was returned {days_late} day(s) late.")
                else:
                    print(f"'{book.title}' was returned on time.")

                book.is_available = True
                book.due_date = None            # The returned copy no longer has a due date
                member.borrowed_books.remove(book)
                return True

        print(f"Book with ID {book_id} was not borrowed by {member.name}.")
        return False

    # Search for one book copy by its unique ID.
    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_available:
                    print(
                        f"Book ID {book.book_id}: '{book.title}' is available "
                        f"at shelf '{book.shelf_location}'."
                    )
                else:
                    print(
                        f"Book ID {book.book_id}: '{book.title}' is currently borrowed "
                        f"and due back on {book.due_date}."
                    )
                return book

        print(f"Book with ID {book_id} was not found.")
        return None


# ==========================================
# DATA
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
# SETUP AND EXAMPLE USE
# ==========================================
library = Library()

for title, author, shelf_location in book_data:
    library.add_book(title, author, shelf_location)

members = {}
for name, member_type in member_data:
    member = library.register_member(name, member_type)
    if member is not None:
        members[name] = member



