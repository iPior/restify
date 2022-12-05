import email
from rest_framework import serializers

from accounts.models import UserExtended, Notification

from django.contrib.auth import password_validation
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExtended
        fields = ['first_name', 'last_name', 'email', 'password', 'phone_num', 'avatar']
        #email and username confusing

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExtended
        fields = ['first_name', 'last_name', 'email', 'phone_num', 'avatar']


'''
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExtended
        fields = ['email', 'password']
        
        def validate(self, data):
            email = data.get("email", None)
            password = data.get("password", None)
            

            if email and password:
                user = authenticate(email=email, password=password)

                if not user:
                    raise serializers.ValidationError("Username or password incorrect")
            else:
                raise serializers.ValidationError("Please enter a email and password")

            data['user']=user
            return user
'''

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = UserExtended
        fields = ['username', 'first_name', 'last_name', 'email', 'password',   'phone_num', 'avatar']


    def create(self, validated_data):
        return UserExtended.objects.create_user(**validated_data)

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields='__all__'

    
