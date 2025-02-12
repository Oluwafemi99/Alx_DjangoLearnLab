# Creating a book
from bookshelf.models import Book
>>> my_book = Book(title='1984', author='George Orwell', publication_year='1949')                  
>>> my_book.save()
>>> 

# Retrieving and Displaying all attributes in Book

>>> Book.objects.all().values()
<QuerySet [{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}]>
>>>

# Updating the title
>>> x = Book.objects.all()[0]
>>> x.title
'1984'
>>> x.title = "Nineteen Eighty-Four"
>>> x.save()
>>> Book.objects.all().values()
<QuerySet [{'id': 1, 'title': 'Nineteen Eighty-Four', 'author': 'George Orwell', 'publication_year': 1949}]>
>>>

# Deleting the Book created and confirming the removal

>>> x = Book.objects.all()[0]      
>>> x.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all().values()
<QuerySet []>
>>>
