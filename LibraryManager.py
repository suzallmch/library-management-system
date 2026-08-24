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

    def checkout(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
        else:
            print(f"The book '{book.title}' is not available for checkout.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
        else:
            print(f"The book '{book.title}' was not borrowed by {self.name}.")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def checkout_book(self, member, title):
        for book in self.books:
            if book.title == title:
                member.checkout(book)
                return
        print(f"The book '{title}' is not found in the library.")

    def return_book(self, member, title):
        for book in self.books:
            if book.title == title:
                member.return_book(book)
                return
        print(f"The book '{title}' is not owned in our library.")


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

library = Library()

# create a Book object for each (title, author) pair, add it to the library
for title, author in book_data:
    new_book = Book(title, author)
    library.add_book(new_book)

# create a Member object for each name, add it to the library,
# and keep a reference in a dict so we can look members up by name later
members = {}
for name in member_names:
    new_member = Member(name)
    library.add_member(new_member)
    members[name] = new_member

# at this point: library.books has 20 Book objects,
# library.members has 5 Member objects,
# and members["Alice"], members["Bob"], etc. let you grab a specific one.