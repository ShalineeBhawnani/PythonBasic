from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Registration

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']

class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        model =User
        fields = ['email']

class ResetPasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['password']