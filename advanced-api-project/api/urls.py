from django.urls import path
from .views import (
    ListView, DetailView, CreateView, UpdateView, DeleteView,
    AuthorList, AuthorDetail, AuthorCreate, AuthorUpdate, AuthorDelete
)

urlpatterns = [
    path('books/', ListView.as_view(), name='book-list'),
    path('books/<int:pk>/', DetailView.as_view(), name='book-detail'),
    path('books/create/', CreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', UpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', DeleteView.as_view(), name='book-delete'),
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('authors/create/', AuthorCreate.as_view(), name='author-create'),
    path('authors/<int:pk>/update/', AuthorUpdate.as_view(), name='author-update'),
    path('authors/<int:pk>/delete/', AuthorDelete.as_view(), name='author-delete'),
]
