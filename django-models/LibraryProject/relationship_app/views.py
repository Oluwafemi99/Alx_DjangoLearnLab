from django.shortcuts import render
from .models import Book, Library
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.template import loader

# Create a function-based view


def list_books(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)


def books(request):
    template = loader.get_template('list_book.html')
    return HttpResponse(template.render())

# class based views


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['average_rating'] = library.get_average_rating()
        return context
