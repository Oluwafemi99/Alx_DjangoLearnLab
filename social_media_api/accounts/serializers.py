from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        models = CustomUser
        fields = "__all__"

    def create(self, validated_data):
        # Create the user with the provided data
        user = get_user_model().objects.create_user(
            username=validated_data.get("username"),
            email=validated_data.get("email"),
            password=validated_data.get("password")
        )
        # Create an authentication token for the user
        Token.objects.create(user=user)
        return user
