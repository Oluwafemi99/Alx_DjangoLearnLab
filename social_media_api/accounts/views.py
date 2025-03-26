from django.shortcuts import render
from rest_framework import generics
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class SignUpView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    authentication_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user
