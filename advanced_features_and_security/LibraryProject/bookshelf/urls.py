from django.urls import path
from . import views

urlpatterns = [
    path("bookshelf", views.book_list, name="bookshelf"),
]
