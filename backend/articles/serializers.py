from rest_framework import serializers
from .models import Post, Object

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "discription", "status", "created_at", "updated_at", "user"]

class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = ["id", "title", "url", "discription", "post_data"]