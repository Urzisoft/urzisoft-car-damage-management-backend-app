from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *


class CarsReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsReport
        fields = '__all__'


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
