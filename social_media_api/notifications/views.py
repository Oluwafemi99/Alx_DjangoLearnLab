from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializers


# Create your views here.
# View to fetch all notifications for the authenticated user.
# Unread notifications are highlighted.
class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipent=self.request.user).order_by('-timestamp')


# View to mark a notification as read.
class MarkNotificationAsReadView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializers
    queryset = Notification.objects.all()

    def patch(self, request, pk):
        notification = self.get_object()
        if notification.recipient != request.user:
            return Response({'error': 'you are not authorised'}, status=400)
        notification.is_read = True
        notification.save()
        return Response({'message': 'Notification marked as read'})
