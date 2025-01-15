from rest_framework import serializers
from users_module.models import User


class UserSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')], required=True, allow_blank=False)

    class Meta:
        model = User
        fields = ['email', 'password', 'gender', 'username', 'is_verified', 'date_joined']
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
            'date_joined': {'read_only': True},
            'is_verified': {'read_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        if password is None:
            raise serializers.ValidationError({"password": "Invalid Data provided."})
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
