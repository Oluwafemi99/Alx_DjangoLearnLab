from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.views.generic.edit import UpdateView, DeleteView
from django.template import loader
from .models import Library
from django.contrib.auth.views import LoginView
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
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
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'


@user_passes_test(lambda u: u.userprofile.role == 'Admin')
class AdminView(TemplateView):
    template_name = 'relationship_app/admin_view.html'


@user_passes_test(lambda u: u.userprofile.role == 'Librarian')
class LibrarianView(TemplateView):
    template_name = 'relationship_app/librarian_view.html'


@user_passes_test(lambda u: u.userprofile.role == 'Member')
class MemberView(TemplateView):
    template_name = 'relationship_app/member_view.html'


@method_decorator(permission_required('relationship_app.can_add_book', raise_exception=True), name='dispatch')
class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'published_date']
    template_name = 'relationship_app/book_form.html'
    success_url = reverse_lazy('book_list')


@method_decorator(permission_required('relationship_app.can_change_book', raise_exception=True), name='dispatch')
class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'published_date']
    template_name = 'relationship_app/book_form.html'
    success_url = reverse_lazy('book_list')


@method_decorator(permission_required('relationship_app.can_delete_book', raise_exception=True), name='dispatch')
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'relationship_app/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
