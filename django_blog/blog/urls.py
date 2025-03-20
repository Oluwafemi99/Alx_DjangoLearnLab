from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import SignUpView, profile_view, Listviews, CreateView, DetailView, DeleteView, UpdateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', SignUpView.as_view(template_name='register.html'), name='register'),
    path('profile/', profile_view, name='profle'),
    path('posts/', Listviews.as_view(template_name='list.html'), name='post'),
    path('posts/new/', CreateView.as_view(template_name='form.html'), name='posts-new'),
    path('posts/<int:pk>/', DetailView.as_view(template_name='detail.html'), name='post-detail'),
    path('posts/<int:pk>/edit', UpdateView.as_view(template_name='form.html'), name='post-edit'),
    path('posts/<int:pk>/delete/', DeleteView.as_view(), name='post-delete')
]


# if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
