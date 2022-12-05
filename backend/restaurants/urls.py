
from django.contrib import admin
from django.urls import include, path
from restaurants.views import MyRestaurantFeed, MyRestaurantInfo, MyRestaurantMenu, MyRestaurantComments, MyRestaurantPhoto, RestaurantPhotoView, RestaurantFeed, RestaurantInfo, RestaurantMenu, RestaurantComments, LikeView, FollowView, AddFollowView, AddLikeView, RestaurantSearchListView

urlpatterns = [
    path('myrestaurant/blogs/', MyRestaurantFeed.as_view()),
    path('myrestaurant/about/', MyRestaurantInfo.as_view(), name='about'),
    path('myrestaurant/menu/', MyRestaurantMenu.as_view()),
    path('myrestaurant/comments/', MyRestaurantComments.as_view()),
    path('myrestaurant/photos/', MyRestaurantPhoto.as_view()),
    path('<int:pk>/followers/', FollowView.as_view()),
    path('<int:pk>/photos/', RestaurantPhotoView.as_view()),
    path('<int:pk>/likes/', LikeView.as_view()),
    path('<int:pk>/blogs/', RestaurantFeed.as_view()),
    path('<int:pk>/about/', RestaurantInfo.as_view()),
    path('<int:pk>/menu/', RestaurantMenu.as_view()),
    path('<int:pk>/comments/', RestaurantComments.as_view()),
    path('<int:pk>/follow/', AddFollowView.as_view()),
    path('<int:pk>/like/', AddLikeView.as_view()),
    path('search/', RestaurantSearchListView.as_view())
]
