from dataclasses import fields
from rest_framework import serializers

from blogs.models import BlogPost, BlogLike
from restaurants.models import Restaurant
from accounts.models import UserExtended

from restaurants.serializers import RestaurantSerializer

class BlogPostSerializer(serializers.ModelSerializer):
    author=serializers.CharField(source='author.id', read_only=True)
    class Meta:
        model = BlogPost
        fields = ['author','title', 'content', 'avatar', 'date_published']

class BlogLikeSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    blog_post=serializers.CharField(read_only=True)
    class Meta:
        model = BlogLike
        fields = ['user', 'blog_post']