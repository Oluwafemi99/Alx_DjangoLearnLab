from .views import list_books
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import SignUpView
from .views import AdminView
from .views import LibrarianView
from .views import MemberView
from .views import BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', views.list_books, name='book_list'),
    path('books/<int:pk>/', views.LibraryDetailView.as_view(), name='book_detail'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('signup/', SignUpView.as_view(template_name='register.html'), name='signup'),
    path('register/', views.register, name='register'),
    path('admin-view/', AdminView.as_view(), name='admin_view'),
    path('librarian-view/', LibrarianView.as_view(), name='librarian_view'),
    path('member-view/', MemberView.as_view(), name='member_view'),
    path('book/add/', BookCreateView.as_view(), name='add_book/'),
    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='edit_book/'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='delete_book'),
]
