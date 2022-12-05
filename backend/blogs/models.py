from distutils.command.upload import upload
from tokenize import blank_re
from django.db import models
from django.utils import timezone
from django.conf import settings


from restaurants.models import Restaurant

# Create your models here.
class BlogPost(models.Model):

    author = models.ForeignKey(
        to=Restaurant, related_name='blogpost', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    avatar = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    date_published = models.DateTimeField(default=timezone.now)
    
class BlogLike(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='bloglike', on_delete=models.CASCADE)
    blog_post = models.ForeignKey(
        to=BlogPost, on_delete=models.CASCADE, related_name='bloglike')
