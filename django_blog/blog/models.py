from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(max_length=220)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # user = User.objects.get(user)
    # user.set_password('password')
    # user.save()

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=350)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
