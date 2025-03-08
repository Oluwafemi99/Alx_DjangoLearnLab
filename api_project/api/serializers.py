from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        models = Book
        feild = "__all__"
