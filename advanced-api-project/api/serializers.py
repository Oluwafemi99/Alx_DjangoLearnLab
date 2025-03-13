from rest_framework import serializers
from .models import Book, Author
from datetime import date


# this is  for serializing and deserializing Book instances.
class BookSerializer(serializers.ModelSerializer):

    class meta:
        model = Book
        field = '__all__'

# ensuring the publication_year is not in the future.
    def validate_publication_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# this is  for serializing and deserializing Author instances.
class AuthorSerializer(serializers.ModelSerializer):
    # The books field uses the BookSerializer to serialize the related books.
    books = BookSerializer(many=True, read_only=True)

    class meta:
        model = Author
        field = ['name', 'books']
