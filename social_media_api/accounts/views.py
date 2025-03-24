from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, status
from django.urls import reverse_lazy
from .serializers import CustomUserSerilizer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import CustomUser


# Create your views here.
class SignUpView(generics.CreateAPIView):
    serializer_class = [CustomUserSerilizer]
    success_url = reverse_lazy('login')

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = CustomUser.objects.get(username=request.data['username'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)


class ProfileView(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = [CustomUserSerilizer]

    def get_object(self):
        return self.request.user
