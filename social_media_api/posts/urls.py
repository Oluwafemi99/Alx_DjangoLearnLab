from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostView, CommentView, FeedView

router = DefaultRouter()
router.register(r'posts', PostView, basename='post')
router.register(r'comments', CommentView, basename='comment')
urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feeds')
]
