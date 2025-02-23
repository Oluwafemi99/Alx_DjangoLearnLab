from .models import Author, Book, Library, Librarian

author_id = 1
books_by_author = Book.objects.filter(author__id=author_id)

# Get all books in the library
books = Library.objects.all()

# Assuming you want to get a librarian by a specific library's ID
librarian = Librarian.objects.get(library__id=1)
