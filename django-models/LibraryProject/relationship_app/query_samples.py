from .models import Author, Book, Library, Librarian

# Query all books by a specific author
author_id = 1  # Replace 1 with the actual author ID
books_by_author = Book.objects.filter(author__id=author_id)

# List all books in a library
library_name = "example_library_name"  # Replace with the actual library name
books = Library.objects.get(name=library_name)
books.all()

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library__id=library_id)
