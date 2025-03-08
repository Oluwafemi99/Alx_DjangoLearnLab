from django.urls import path, include
from . import views
from .views import BookListCreateAPIView
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, CommentViewset

router = DefaultRouter()
router.register(r'Books', BookViewSet)
router.register(r"comment", CommentViewset)

urlpatterns = [
    path("bookshelf", views.index, name="bookshelf"),
    # path("api/books", BookListCreateAPIView.as_view(), name="book_list_"),
    path('api/', include(router.urls)),
    # Add any additional non-viewset-based endpoints here
]
