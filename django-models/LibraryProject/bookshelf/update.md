# Updating the title
>>> book = Book.objects.all()[0]
>>> book.title
'1984'
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> Book.objects.all().values()
<QuerySet [{'id': 1, 'title': 'Nineteen Eighty-Four', 'author': 'George Orwell', 'publication_year': 1949}]>
>>>
