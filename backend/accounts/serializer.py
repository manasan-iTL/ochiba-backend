from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["id", "username", "image"]
