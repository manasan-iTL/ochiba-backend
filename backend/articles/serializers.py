from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import Post, Object
from accounts.serializer import UserSerializer


"""
    Postに関連するObjectsを検証するフィールドを追加する
    →他のSerializerをフィールドとして扱うことが可能
    →SerializerMethodField()
    →読み取りはできる、書き込みは不明

    追加処理として、get_[fields名]の関数を定義し、ObjectsのデータをSerializer内部で
    取得する

"""

class ObjectIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = ["id", "title", "url"]

class ArticlesIndexSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    objects = SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "title", "discription", "status", "created_at", "updated_at", "user", "objects"]
    
    def get_objects(self, post):
        try:
            objects_based_on_post = ObjectIndexSerializer(Object.objects.only("id", "title", "url").filter(post_data = Post.objects.get(id=post.id))[:3], many=True).data
            return objects_based_on_post
        except:
            objects_based_on_post = None
            return objects_based_on_post


class ObjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = ["id", "title", "url", "discription", "post_data"]


class ArticleRequestDetailSerializer(serializers.ModelSerializer):

    objects = ObjectDetailSerializer(many=True)

    class Meta:
        model = Post
        fields = ["id", "title", "discription", "status", "created_at", "updated_at", "user", "objects"]
    
    def create(self, validated_data):

        list_objects = []
        result_response = {}

        # objectsだけ取り出す
        objects = validated_data.pop("objects")

        # Postを登録する
        post = super().create(validated_data)
        result_response["post_id"] = post.id

        # Serializerを通すと、OrderDict型で返ってくるためdict()で普通の辞書型へ変換する
        # 各要素にpost.idを追加する

        for object in objects:
            dictionary = dict(object)
            dictionary["post_data"] = post.id
            list_objects.append(dictionary)

        # objectのSerializerを呼ぶ
        objectSerializer = ObjectDetailSerializer(data=list_objects, many=True)

        # Validation（例外処理がAPIView内でないと動かない可能性あり→呼ばれる）
        if objectSerializer.is_valid(raise_exception=True):
            objectSerializer.save()
            return result_response


class ArticleResponseDetailSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    objects = SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "title", "discription", "status", "created_at", "updated_at", "user", "objects"]

    def get_objects(self, post):
        try:
            objects_based_on_post = ObjectDetailSerializer(Object.objects.filter(post_data = Post.objects.get(id=post.id)), many=True).data
            return objects_based_on_post
        except:
            objects_based_on_post = None
            return objects_based_on_post