from django.urls import path
from . import views

urlpatterns = [
    path("bookshelf", views.index, name="bookshelf"),
]
