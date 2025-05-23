from django.urls import path
from django.contrib.auth.views import LoginView
from .views import SignUpView, ProfileView, FollowUserView, UnfollowUserView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='auth-token'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='following'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow'),
]
