from rest_framework import serializers
from models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'role', 'gender','isVerified']
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True, 'required': True},
            'date_joined': {'read_only': True},
            'last_login': {'read_only': True},
            'phone_number': {'required': True},
            'isVerified': {'required': False}
        }
    pass
