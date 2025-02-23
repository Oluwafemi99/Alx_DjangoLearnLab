from .models import Author, Book, Library, Librarian

books = Library.objects.get(name='library_name')
books.all()
