from rest_framework import serializers
from .models import Book, Comment
from datetime import datetime


class BookSerializer(serializers.ModelSerializer):
    no_of_days = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'
        custom_feilds = "no_of_days"

    def get_no_of_days(self, obj):
        return (datetime.now() - obj.created_at).days


class CommentSerializer(serializers.ModelSerializer):
    day_created = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        feilds = "__all__"
        custom_feilds = "day_created"

        def day_created(self, obj):
            return (datetime.now() - obj.created_at.days)
