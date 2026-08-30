class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other_book):
        return self.author == other_book.author and self.title == other_book.title

    def __ne__(self, other_book):
            return self.author != other_book.author and self.title != other_book.title

    def __lt__(self, other_book):
        return self.pages < other_book.pages

    def __gt__(self, other_book):
        return self.pages > other_book.pages

    def __add__(self, other_book):
        return self.pages + other_book.pages

    def __sub__(self, other_book):
        return self.pages - other_book.pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, pages={self.pages})"

    


book1 = Book("Harry Potter", "JK Rowling", 230)
book2 = Book("Hobbit", "JRRT", 310)
book3 = Book("The Fantastic Tales", "Howly Mangrove", 349)

print(book1)
print(book1 != book2)
print(book2 < book3)
print(book2 > book3)
print(book1+book3)
print("Tales" in book3)
print(repr(book2))