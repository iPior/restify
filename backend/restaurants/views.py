from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView 
from rest_framework.response import Response

from blogs.serializers import BlogPostSerializer
from blogs.models import BlogPost
from restaurants.models import Restaurant, Food, Comment, Follow, Like, Photo
from restaurants.serializers import RestaurantSerializer, FoodSerializer, CommentSerializer, FollowSerializer, LikeSerializer, PhotoSerializer
from restaurants.paginations import RestaurantPagination
from accounts.models import UserExtended, Notification
from rest_framework import filters
# Create your views here.

class MyRestaurantFeed(ListCreateAPIView):
    serializer_class=BlogPostSerializer
    ordering=['-date_published']
    permission_classes=[IsAuthenticated]
    pagination_class = RestaurantPagination

    def get_queryset(self):
        user= self.request.user
        restaurant = Restaurant.objects.get(owner=user)
        return BlogPost.objects.filter(author=restaurant.id)

    def perform_create(self, serializer):
        restaurant = Restaurant.objects.get(owner=self.request.user)
        followers=Follow.objects.filter(restaurant=restaurant)
        post = serializer.save(author = restaurant)
        for follow in followers:
            notification = Notification.objects.create(type=3, from_user=restaurant.owner, to_user=follow.user, post = post)

class MyRestaurantInfo(RetrieveUpdateAPIView):
    serializer_class=RestaurantSerializer
    permission_classes=[IsAuthenticated]

    def get_object(self):
        user= self.request.user
        return get_object_or_404(Restaurant, owner=user)

class MyRestaurantMenu(ListCreateAPIView):
    serializer_class=FoodSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user= self.request.user
        restaurant = Restaurant.objects.get(owner=user)
        return Food.objects.filter(restaurant=restaurant.id)

    def perform_create(self, serializer):
        restaurant = Restaurant.objects.get(owner=self.request.user)
        followers=Follow.objects.filter(restaurant=restaurant)
        for follow in followers:
            notification = Notification.objects.create(type=5, from_user=restaurant.owner, to_user=follow.user)
        serializer.save(restaurant = restaurant)

class MyRestaurantComments(ListAPIView):
    serializer_class=CommentSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user= self.request.user
        restaurant = Restaurant.objects.get(owner=user)
        return Comment.objects.filter(restaurant=restaurant.id)

class RestaurantFeed(ListAPIView):
    serializer_class=BlogPostSerializer
    pagination_class = RestaurantPagination
    #permission_classes=[IsAuthenticated]
    ordering=['-date_published']

    def get_queryset(self):
        return BlogPost.objects.filter(author=self.kwargs['pk'])

class RestaurantInfo(RetrieveAPIView):
    serializer_class=RestaurantSerializer
    #permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Restaurant.objects.filter(id=self.kwargs['pk'])

class RestaurantMenu(ListAPIView):
    serializer_class=FoodSerializer
    #permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Food.objects.filter(restaurant=self.kwargs['pk'])

class RestaurantComments(ListCreateAPIView):
    serializer_class=CommentSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(restaurant=self.kwargs['pk'])
    
    def perform_create(self, serializer):
        restaurant = Restaurant.objects.get(id=self.kwargs['pk'])
        comment = serializer.save(restaurant=restaurant, user=self.request.user)
        notification = Notification.objects.create(type=2, from_user=self.request.user, to_user=restaurant.owner, comment=comment)

class AddFollowView(CreateAPIView):
    serializer_class=FollowSerializer
    permission_classes=[IsAuthenticated]
    queryset=Follow.objects.all()

    def perform_create(self, serializer):
        restaurant = Restaurant.objects.get(id=self.kwargs['pk'])
        notification = Notification.objects.create(type=4, from_user=self.request.user, to_user=restaurant.owner)
        serializer.save(restaurant=restaurant, user=self.request.user)

class AddLikeView(ListAPIView):
    serializer_class=LikeSerializer
    permission_classes=[IsAuthenticated]
    queryset=Like.objects.all()

    def perform_create(self, serializer):
        restaurant = Restaurant.objects.get(id=self.kwargs['pk'])
        notification = Notification.objects.create(type=1, from_user=self.request.user, to_user=restaurant.owner)
        serializer.save(restaurant=restaurant, user=self.request.user)

class FollowView(ListAPIView):
    serializer_class=FollowSerializer
    #permission_classes=[IsAuthenticated]

    def get_queryset(self):
        followers = Follow.objects.filter(restaurant = self.kwargs['pk'])
        return followers
    

class LikeView(ListAPIView):
    serializer_class= LikeSerializer
    #permission_classes=[IsAuthenticated]

    def get_queryset(self):
        likes = Like.objects.filter(restaurant=self.kwargs['pk'])
        return likes

class RestaurantSearchListView(ListAPIView):
    serializer_class=RestaurantSerializer
    #permission_classes=[IsAuthenticated]

    def get_queryset(self):
        query=self.request.GET.get('search')
        menu=Food.objects.filter(Q(name__icontains=query))
        if menu:
            list=Restaurant.objects.none()
            for item in menu:
                list = list | Restaurant.objects.filter(id=item.restaurant_id)
            return list
        return Restaurant.objects.filter(Q(name__icontains=query)|Q(address__icontains=query))


class RestaurantPhotoView(ListAPIView):
    serializer_class=PhotoSerializer
    ordering=['-date_published']
    pagination_class = RestaurantPagination
    
    def get_queryset(self):
        photos = Photo.objects.filter(restaurant=self.kwargs['pk'])
        return photos

class MyRestaurantPhoto(ListCreateAPIView):
    serializer_class=PhotoSerializer
    ordering=['-date_published']
    permission_classes=[IsAuthenticated]
    pagination_class = RestaurantPagination

    def get_queryset(self):
        user= self.request.user
        restaurant = Restaurant.objects.get(owner=user)
        return Photo.objects.filter(restaurant=restaurant)

    def perform_create(self, serializer):
        restaurant = Restaurant.objects.get(owner=self.request.user)
        followers=Follow.objects.filter(restaurant=restaurant)
        photo = serializer.save(restaurant = restaurant)
        for follow in followers:
            notification = Notification.objects.create(type=6, from_user=restaurant.owner, to_user=follow.user)