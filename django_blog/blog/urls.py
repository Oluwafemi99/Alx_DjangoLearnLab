from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import SignUpView, profile_view, ListView, CreateView, DetailView, DeleteView, UpdateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', SignUpView.as_view(template_name='register.html'), name='register'),
    path('profile/', profile_view, name='profle'),
    path('post/', ListView.as_view(template_name='post_list.html'), name='post'),
    path('post/new/', CreateView.as_view(template_name='post_create.html'), name='posts-new'),
    path('post/<int:pk>/', DetailView.as_view(template_name='post_detail.html'), name='post-detail'),
    path('post/<int:pk>/update/', UpdateView.as_view(template_name='post_update.html'), name='post-edit'),
    path('post/<int:pk>/delete/', DeleteView.as_view(template_name='post_delete.html'), name='post-delete'),
]

# if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
