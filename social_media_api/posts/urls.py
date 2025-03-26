from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostView, CommentView

router = DefaultRouter
router.register(r'posts', PostView)
router.register(r'comments', CommentView)
urlparttern = router.urls
