from rest_framework import serializers
# from users_management.models import User
# from djoser.serializers import UserCreateSerializer
#
#
# class UserSerializer(UserCreateSerializer):
#     class Meta(UserCreateSerializer.Meta):
#         fields = ['email', 'password', 'gender']
#
#
# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=True)
#     password = serializers.CharField(write_only=True, required=True)


from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from .models import Customer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = Customer
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'gender', 'profile_picture')


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = Customer
        fields = ('id', 'username', 'first_name', 'last_name', 'gender', 'profile_picture', 'is_active')
