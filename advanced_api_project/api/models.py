from django.db import models

# Create your models here.


# The Author model represents an author with a name.
class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# The Book model represents a book with a title, publication year, and a foreign key to the author.
class Book(models.Model):
    title = models.CharField(max_length=50)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='Books')

    def __str__(self):
        return self.title
