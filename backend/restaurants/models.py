from pydoc import describe
from pyexpat import model
from urllib import request
from django.db import models
from django.conf import settings
from django.utils import timezone

# from accounts.models import UserExtended


# Create your models here.
class Restaurant(models.Model):
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    postal_code = models.CharField(max_length=6)
    address = models.CharField(max_length=120)
    email = models.EmailField()
    phone_num = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to='store_avatars/', null=True, blank=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='user', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(
        to=Restaurant, on_delete=models.CASCADE, related_name='comment')
    comment = models.TextField()

class Food(models.Model):
    name = models.CharField(max_length=120)
    price = models.CharField(max_length=120)
    section = models.CharField(max_length=120)
    description = models.TextField()
    restaurant = models.ForeignKey(
        to=Restaurant, on_delete=models.CASCADE, related_name='food')

class Follow(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='follow', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(
        to=Restaurant, on_delete=models.CASCADE, related_name='follow')

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='like', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(
        to=Restaurant, on_delete=models.CASCADE, related_name='like')

class Photo(models.Model):
    restaurant=models.ForeignKey(to=Restaurant, on_delete=models.CASCADE, related_name='photo')
    photo = models.ImageField(upload_to='store_avatars/', null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

