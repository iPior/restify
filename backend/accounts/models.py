from distutils.command.upload import upload
from enum import unique
from importlib.metadata import requires
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.conf import settings
from django.utils import timezone

from blogs.models import BlogPost
from restaurants.models import Comment

# Create your models here.
class UserExtended(AbstractUser):
    # ---- User comes with first, last, pass, username

    # ---- Adding avatar, feed, following
    username = models.CharField(max_length=120, default='User', unique=True)
    email = models.EmailField(verbose_name="email", unique=True)
    phone_num = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to='profile_avatars/', null=True, blank=True)


class Notification(models.Model):
    #1=Like, 2=Comment, 3=Post, 4=Follow, 5=Menu, 6=photo
    type = models.IntegerField()
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notification_to', on_delete=models.CASCADE)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notification_from', on_delete=models.CASCADE)
    post=models.ForeignKey(BlogPost, related_name='notification_blog', on_delete=models.CASCADE, null=True)
    comment=models.ForeignKey(Comment, related_name='notification_comment', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=timezone.now)