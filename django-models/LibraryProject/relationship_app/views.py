from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.template import loader
from .models import Library
from django.contrib.auth.views import LoginView
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login

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

# user login, logout, and registration


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'


urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/register.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('signup/', SignUpView.as_view(template_name='login.html'), name='signup'),
]
