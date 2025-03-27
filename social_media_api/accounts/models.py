from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(max_length=220, blank=True)
    profile_picture = models.ImageField()
    followers = models.ManyToManyField('self', symmetrical=False, related_name='user_followers')
    following = models.ManyToManyField('self', symmetrical=False, related_name='user_following')
    # Avoids conflict with auth.User.groups
    groups = models.ManyToManyField('auth.Group', related_name='customer_set', blank=True)
    # Avoids conflict with auth.User.user_permissions
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customer_set', blank=True)

    def __str__(self):
        return self.username
