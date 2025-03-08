from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()


class Comment(models.Model):
    name = models.CharField(max_length=255, null=True)
    comment = models.CharField(max_length=255)
    flagged = models.BooleanField(default=False)
