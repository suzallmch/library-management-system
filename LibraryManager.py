# ==========================================
# CLASS DEFINITIONS (the blueprints)
# ==========================================

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
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
    def add_book(self, title, author):
        new_book = Book(title, author)
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
                    print(f"Book '{title}' is available in the library.")
                else:
                    print(f"Book '{title}' is not available in the library.")
                return
        print(f"Book '{title}' is not found in the library.")


# ==========================================
# DATA (raw values used to create objects)
# ==========================================

book_data = [
    ("Dune", "Frank Herbert"),
    ("1984", "George Orwell"),
    ("Brave New World", "Aldous Huxley"),
    ("The Hobbit", "J.R.R. Tolkien"),
    ("Fahrenheit 451", "Ray Bradbury"),
    ("The Great Gatsby", "F. Scott Fitzgerald"),
    ("Animal Farm", "George Orwell"),
    ("Moby Dick", "Herman Melville"),
    ("War and Peace", "Leo Tolstoy"),
    ("Crime and Punishment", "Fyodor Dostoevsky"),
    ("The Catcher in the Rye", "J.D. Salinger"),
    ("To Kill a Mockingbird", "Harper Lee"),
    ("Pride and Prejudice", "Jane Austen"),
    ("The Odyssey", "Homer"),
    ("Frankenstein", "Mary Shelley"),
    ("Dracula", "Bram Stoker"),
    ("The Picture of Dorian Gray", "Oscar Wilde"),
    ("Slaughterhouse-Five", "Kurt Vonnegut"),
    ("The Alchemist", "Paulo Coelho"),
    ("Neuromancer", "William Gibson"),
]

member_names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]


# ==========================================
# SETUP PHASE (build the world — create real
# objects from the blueprints + data above)
# ==========================================

library = Library()  # creates a Library object, which will hold all the books and members

# add_book takes (title, author) directly and builds the Book internally,
# so we just pass the raw values through — no need to build Book ourselves
for title, author in book_data:
    library.add_book(title, author)

# register_member takes a name directly and builds the Member internally,
# and we keep a reference in a dict so we can look members up by name later
members = {}
for name in member_names:
    library.register_member(name)
    members[name] = library.members[-1]  # grab the member we just added

# at this point: library.books has 20 Book objects,
# library.members has 5 Member objects,
# and members["Alice"], members["Bob"], etc. let you grab a specific one.