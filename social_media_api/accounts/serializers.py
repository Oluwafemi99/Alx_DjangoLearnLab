from rest_framework import serializers
from .models import CustomUser


class CustomUserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        feilds = '__all__'
