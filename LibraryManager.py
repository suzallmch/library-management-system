# ==========================================
# CLASS DEFINITIONS (the blueprints)
# ==========================================

class Book:
    def __init__(self, title, author, shelf_location):
        self.title = title
        self.author = author
        self.shelf_location = shelf_location
        self.is_available = True


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    # add a new book to the library
    def add_book(self, title, author, shelf_location):
        new_book = Book(title, author, shelf_location)
        self.books.append(new_book)

    # add a new member to the library
    def register_member(self, name):
        new_member = Member(name)
        self.members.append(new_member)

    # borrow a book from the library
    def borrow_book(self, member, title):
        for book in self.books:
            if book.title == title and book.is_available:
                book.is_available = False
                member.borrowed_books.append(book)
                return True
        print(f"Book '{title}' is not available for borrowing.")
        return False

    # a member returns a book to the library
    def return_book(self, member, title):
        for book in member.borrowed_books:
            if book.title == title:
                book.is_available = True
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
                    print(f"Book '{title}' is not available in the library.")
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

member_names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]


# ==========================================
# SETUP PHASE (build the world — create real
# objects from the blueprints + data above)
# ==========================================

library = Library()  # creates a Library object, which will hold all the books and members

# add_book takes (title, author) directly and builds the Book internally,
# so we just pass the raw values through — no need to build Book ourselves
for title, author, shelf_location in book_data:
    library.add_book(title, author, shelf_location)

# register_member takes a name directly and builds the Member internally,
# and we keep a reference in a dict so we can look members up by name later
members = {}
for name in member_names:
    library.register_member(name)
    members[name] = library.members[-1]  # grab the member we just added

# at this point: library.books has 20 Book objects,
# library.members has 5 Member objects,
# and members["Alice"], members["Bob"], etc. let you grab a specific one.