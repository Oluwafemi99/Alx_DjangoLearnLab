from django.shortcuts import render
from .models import Author, Book, Library, Librarian
from django.views.generic import DetailView
# Create a function-based view


def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)

# class based views


class BookDetailView(DetailView):
    model = Library
    template_name = 'books/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        context['average_rating'] = book.get_average_rating()
        return context
