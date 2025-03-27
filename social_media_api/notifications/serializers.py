from .models import Notification
from rest_framework import serializers


class NotificationSerializers(serializers.ModelSerializer):

    class Meta:
        model = Notification
        feilds = '__all__'
