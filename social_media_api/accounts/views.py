from django.shortcuts import render
from rest_framework import generics
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# Create your views here.
class SignUpView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    authentication_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user


class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    # view to allow user to follow another user
    def post(self, request, username):
        follow_user = get_object_or_404(CustomUser, username)
        if follow_user == request.user:
            return Response({'error': 'you cannt follow yourself'}, status=400)
        request.user.following.add(follow_user)
        return Response(f'you are now following {username}', status=200)


class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, username):
        unfollow_user = get_object_or_404(CustomUser, username)
        if unfollow_user == request.user:
            return Response({'error': 'you cannot unfollow yourself'})
        request.user.following.remove(unfollow_user)
        return Response({f'you have succesfully unfollowed {username}.'})
