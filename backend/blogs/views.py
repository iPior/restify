from django.shortcuts import render, get_object_or_404

from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.views import APIView 
from rest_framework.response import Response

from blogs.models import BlogPost, BlogLike
from restaurants.models import Restaurant
from blogs.serializers import BlogPostSerializer, BlogLikeSerializer
from accounts.models import UserExtended, Notification
from accounts.serializers import NotificationSerializer
from restaurants.models import Follow


#Permission
class IsOwnerOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        restaurant = Restaurant.objects.get(owner=request.user)
        return obj.author == restaurant
# Create your views here.
class BlogFeed(ListAPIView):
    serializer_class=NotificationSerializer
    ordering=['-date_published']
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user= self.request.user
        return Notification.objects.filter(to_user=user)

class BlogView(RetrieveUpdateAPIView):
    serializer_class=BlogPostSerializer
    permission_classes=[IsAuthenticated, IsOwnerOrReadOnly]
    
    def get_object(self):
        return get_object_or_404(BlogPost, id=self.kwargs['id'])

class BlogLikeView(ListCreateAPIView):
    serializer_class=BlogLikeSerializer
    #permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return BlogLike.objects.filter(blog_post=self.kwargs['id'])

    def perform_create(self, serializer):
        post = BlogPost.objects.get(id=self.kwargs['id'])
        notification = Notification.objects.create(type=1, from_user=post.author.owner, to_user=self.request.user, post=post)
        serializer.save(blog_post=post, user=self.request.user)