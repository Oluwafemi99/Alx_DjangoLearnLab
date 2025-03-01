from .models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "example_author_name" 
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

# List all books in a library
library_name = "example_library_name"  # Replace with the actual library name
books = Library.objects.get(name=library_name)
books.all()

# Retrieve the librarian for a library
liberian_name = "example_library_name"
librarian = Librarian.objects.get(library=liberian_name)
