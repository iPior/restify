from cProfile import Profile
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, FormView
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.db import IntegrityError


from rest_framework import viewsets, status, response
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from accounts.models import UserExtended, Notification
from accounts.serializers import RegisterSerializer, UserSerializer, ProfileSerializer, NotificationSerializer
from accounts.paginations import NotificationPagination

from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer
from restaurants.views import MyRestaurantInfo


#------ PROFILE VIEWS
class ProfileView(RetrieveAPIView):
    model = UserExtended
    serializer_class=ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(UserExtended, id=self.request.user.id)

class UpdateProfileView(RetrieveAPIView, UpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Profile, id=self.request.user.id)


#------ REGISTER VIEW
class RegisterView(CreateAPIView): 
    serializer_class = RegisterSerializer
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        

        if serializer.is_valid():
            serializer.save()
            
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return response.Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


#------ LOGIN/LOGOUT VIEWS
'''
class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)# LoginSerializer(data=request.data)
        serializer.is_valid() #issue
        user = serializer.validate_data['user']

        token, created = Token.objects.get_or_create(user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
'''


class LogoutView(RetrieveAPIView):
    def get(self, request):
        if authenticate(request):
            logout(request)

class NotificationView(ListAPIView):
    serializer_class= NotificationSerializer
    permission_classes=[IsAuthenticated]
    pagination_class=NotificationPagination

    def get_queryset(self):
        user = self.request.user
        return  Notification.objects.filter(to_user=user)

class CreateRestaurantView(CreateAPIView):
    serializer_class=RestaurantSerializer
    permission_classes=[IsAuthenticated]
    queryset=Restaurant.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except IntegrityError:
            return Response({'error':'You already have a restaurant'})
    def perform_create(self, serializer):
        data = self.request.data
        serializer.save(name = data['name'], address=data['address'], postal_code=data['postal_code'], avatar=data['avatar'], email=data['email'], phone_num=data['phone_num'], description=data['description'],owner=self.request.user)