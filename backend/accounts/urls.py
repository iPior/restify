
from django.contrib import admin
from django.urls import include, path

from accounts.views import RegisterView, UpdateProfileView, ProfileView, NotificationView, CreateRestaurantView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('login/token_refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/view/', ProfileView.as_view(), name='profile_view'),
    path('profile/edit/', UpdateProfileView.as_view(), name='update_profile_view'),
    path('profile/notification/', NotificationView.as_view(), name='notification_view'),
    path('profile/addrestaurant/', CreateRestaurantView.as_view(), name='create_restaurant_view'),
]