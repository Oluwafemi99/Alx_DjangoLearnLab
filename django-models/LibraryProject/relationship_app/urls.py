from .views import list_books
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.LibraryDetailView.as_view(), name='book_detail'),
]
