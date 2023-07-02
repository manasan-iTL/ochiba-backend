from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import Post, Object

class PostSerializer(serializers.ModelSerializer):

"""
    Postに関連するObjectsを検証するフィールドを追加する
    →他のSerializerをフィールドとして扱うことが可能
    →SerializerMethodField()
    →読み取りはできる、書き込みは不明

    追加処理として、get_[fields名]の関数を定義し、ObjectsのデータをSerializer内部で
    取得する

"""

class PostsIndexSerializer(serializers.ModelSerializer):

    objects = SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "title", "discription", "status", "created_at", "updated_at", "user", "objects"]
    
    def get_objects(self, post):
        try:
            objects_based_on_post = ObjectSerializer(Object.objects.filter(post_data = Post.objects.get(id=post.id))[:3], many=True).data
            return objects_based_on_post
        except:
            objects_based_on_post = None
            return objects_based_on_post

class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = ["id", "title", "url", "discription", "post_data"]