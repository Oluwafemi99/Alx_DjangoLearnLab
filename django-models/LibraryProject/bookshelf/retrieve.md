from bookshelf.models import Book
# Retrieving and Displaying all attributes in Book

>>> my_book = Book.objects.get(title='1984')
>>> my_book.id, my_book.title, my_book.author, my_book.publication_year
(1, '1984', 'George Orwell', 1949)
