# query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# Create sample data
author = Author.objects.create(name="Chinua Achebe")
book1 = Book.objects.create(title="Things Fall Apart", author=author)
book2 = Book.objects.create(title="No Longer at Ease", author=author)

library = Library.objects.create(name="National Library")
library.books.add(book1, book2)

librarian = Librarian.objects.create(name="Grace", library=library)

# Query all books by a specific author
books_by_author = Book.objects.filter(author__name="Chinua Achebe")
print("Books by Chinua Achebe:")
for book in books_by_author:
    print(f"- {book.title}")

# List all books in a library
books_in_library = library.books.all()
print("\nBooks in National Library:")
for book in books_in_library:
    print(f"- {book.title}")

# Retrieve the librarian for a library
librarian_for_library = library.librarian
print(f"\nLibrarian for {library.name}: {librarian_for_library.name}")
