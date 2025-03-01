from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

# Create your views here.


@permission_required("bookshelf.can_edit", raise_exception=True)
def book_list(request):
    all_books = [
        {"id": 1, "title": "python", "author": "Femi"},
        {"id": 2, "title": "django", "author": "Tolu"}
    ]
    return render(request, "bookshelf/book_list.html", {"all_books": all_books})
