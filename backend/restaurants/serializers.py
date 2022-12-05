from rest_framework import serializers

from restaurants.models import Restaurant, Comment, Food, Like, Follow, Photo

class RestaurantSerializer(serializers.ModelSerializer):
    restaurant=serializers.CharField(source='restaurant.id', read_only=True)
    owner=serializers.CharField(read_only=True)
    class Meta:
        model = Restaurant
        fields = ['restaurant', 'owner', 'name', 'description', 'postal_code', 'address', 'email', 'phone_num', 'avatar']

class CommentSerializer(serializers.ModelSerializer):
    restaurant=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta: 
        model = Comment
        fields = ['user', 'restaurant', 'comment']

class FoodSerializer(serializers.ModelSerializer):
    restaurant=serializers.CharField(read_only=True)
    #restaurant_address = restaurant.address
    class Meta:
        model = Food
        fields = ['name', 'price', 'section', 'description', 'restaurant'] 

class FollowSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    restaurant=serializers.CharField(read_only=True)
    class Meta:
        model = Follow
        fields = ['user', 'restaurant']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'restaurant']

class PhotoSerializer(serializers.ModelSerializer):
    restaurant = serializers.CharField(read_only=True)
    class Meta:
        model = Photo
        fields = '__all__'
