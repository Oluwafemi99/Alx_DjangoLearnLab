from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Post, Comment, Like
from . serializers import PostSerializer, CommentSerializer
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from .pagination import PostPagination, CommentPagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType


# Create your views here.
class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    pagination_class = PostPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    SearchFilter = ['title', 'content']


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    pagination_class = CommentPagination

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)

        Notification.objects.create(recipient=comment.post.author, actor=self.request.user, verb="commented on your post", target=comment.post)


class FeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    # Class-based view to generate a feed of posts from users the current user follows.
    # The posts are ordered by creation date, with the most recent posts at the top.
    def get_queryset(self):
        # Get the users the current user is following
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')


class LikePostView(generics.GenericAPIView):
    queryset = Like.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        # Check if the user has already liked the post
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({'error': 'you already liked this post'})
        Like.objects.get_or_create(user=request.user, post=post)

        # generate a notification
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target_content_type=ContentType.objects.get_for_model(post),
            target_object_id=post.id,
        )


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Like.objects.all()

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        # Check if the user has liked the post
        like = Like.objects.filter(user=request.user, post=post).first()
        if not like:
            return Response({"error": "you have not liked this post"})

        like.delete()
        return Response({"post unliked successfully"})
