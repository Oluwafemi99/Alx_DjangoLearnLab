from .models import Author, Book, Library, Librarian

author = Author.objects.get(Book)
books = Library.objects.all()
liberian = Library.objects.get(Library=Librarian)
