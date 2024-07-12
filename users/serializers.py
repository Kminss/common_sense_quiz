from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, CharField

from .models import User


class SignupSerializer(ModelSerializer):
    """
    1. signup과 관련된 validation 수행
    2. create override
    """

    class Meta:
        model = get_user_model()
        fields = ("username", "nickname", "password")

    def create(self, validated_data):
        password = validated_data.pop('password')
        # NOT init password in User model (set_password 통해서)
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(ModelSerializer):
    """
    login과 관련된 validation 수행
    """

    class Meta:
        model = get_user_model()
        fields = ("username", "password")

    username = CharField(required=True)
    password = CharField(required=True)
