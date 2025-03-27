from django.urls import path
from .views import NotificationListView, MarkNotificationAsReadView

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notifications'),
    path('notifications_read/', MarkNotificationAsReadView.as_view(), name='notifications_read'),
]
