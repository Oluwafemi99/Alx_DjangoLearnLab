from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    bio = models.TextField(max_length=250, blank=True)
    profile_picture = models.ImageField(upload_to='picture', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')

    # add Releted_name to avoid permission clashes
    groups = models.ManyToManyField('auth.Group', related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customuser_permissions_set', blank=True)

    class Meta:
        permissions = [
            ('can_follow', 'Can follow other users')
        ]
