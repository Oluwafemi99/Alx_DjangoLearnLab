from .views import list_books
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import SignUpView

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.LibraryDetailView.as_view(), name='book_detail'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('signup/', SignUpView.as_view(template_name='registration/signup.html'), name='signup'),
    path('register/', views.register, name='register'),
]
