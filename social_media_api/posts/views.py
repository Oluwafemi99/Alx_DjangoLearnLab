from django.shortcuts import render
from rest_framework import viewsets ,generics
from .models import Post, Comment
from . serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly
from .pagination import PostPagination, CommentPagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    pagination_class = PostPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    SearchFilter = ['title', 'content']


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    pagination_class = CommentPagination


class FeedView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    # Class-based view to generate a feed of posts from users the current user follows.
    # The posts are ordered by creation date, with the most recent posts at the top.
    def get_queryset(self):
        # Get the users the current user is following
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
