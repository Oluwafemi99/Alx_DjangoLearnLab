# Deleting the Book created and confirming the removal

>>> book = Book.objects.all()[0]      
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all().values()
<QuerySet []>
>>>
