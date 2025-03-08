from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets
from .models import Book, Comment
from .serializers import BookSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


def index(request):
    return HttpResponse(render("Welcome to my book shelf."))


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=True, methods=['post'])
    def flag(self, request, pk=None):
        comment = self.get_object()
        comment.flagged = True
        comment.save()
        return Response({'status': 'comment flagged'}, status=status.HTTP_200_OK)