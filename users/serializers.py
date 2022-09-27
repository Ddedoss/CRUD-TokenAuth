from rest_framework import serializers
from django.contrib.auth.models import User


class UsersReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'first_name', 'last_name',
                  'email', 'last_login', 'is_active', 'date_joined'
                  )


class UsersWriteOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name',
                  'last_name', 'email'
                  )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
