from .models import Author, Book, Library, Librarian

# Query all books by a specific author
author_id = 1  # Replace 1 with the actual author ID
books_by_author = Book.objects.filter(author__id=author_id)

# List all books in a library
library_id = 1  # Replace 1 with the actual library ID
library_books = Book.objects.filter(library__id=library_id)

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library__id=library_id)
