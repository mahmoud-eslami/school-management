from  rest_framework import serializers
from  django.contrib.auth.models import User
from datetime import datetime

class NewsSerializer(serializers.Serializer):
    id = serializers.CharField(allow_null=False,allow_blank=False,max_length=10)
    title = serializers.CharField(max_length=20,allow_blank=False,allow_null=True)
    content = serializers.CharField(max_length=200,allow_blank=False,allow_null=True)
    author_id = serializers.CharField(allow_null=False,allow_blank=False,max_length=10)
    pic = serializers.ImageField()
    release_date = serializers.DateTimeField()

    def create(self , validated_data):
        return News.objects.create(validated_data)

    def update(self ,instance , validated_data):
        instance.title = validated_data.get('title' , instance.title)
        instance.content = validated_data.get('content' , instance.content)
        instance.pic = validated_data.get('title' , instance.pic)
        instance.title = validated_data.get('title' , instance.title)
        instance.save()
        return instance

class allNewsSerializer(serializers.Serializer):
    author_id = serializers.CharField(required = True,allow_null=False,allow_blank=False,max_length=10)
    id = serializers.CharField(required = True,allow_null=False,allow_blank=False,max_length=10)
    title = serializers.CharField(required=True,allow_null=False,allow_blank=False,max_length=200)
    content = serializers.CharField(required=True,allow_null=False,allow_blank=False,max_length=2048)
    release_date = serializers.DateTimeField(required=True,allow_null=False)
    pic = serializers.ImageField(required=True,allow_null=True,allow_empty_file=True)

class editNewsSerializer(serializers.Serializer):
    id = serializers.CharField(required = True,allow_null=False,allow_blank=False,max_length=10)
    title = serializers.CharField(required=True,allow_null=False,allow_blank=False,max_length=200)
    content = serializers.CharField(required=True,allow_null=False,allow_blank=False,max_length=2048)
    pic = serializers.ImageField(required=True,allow_null=True,allow_empty_file=True)

class addNewsSerializer(serializers.Serializer):
    author_id = serializers.CharField(required = True,allow_null=False,allow_blank=False,max_length=10)
    title = serializers.CharField(required=True,allow_null=False,allow_blank=False,max_length=200)
    content = serializers.CharField(required=True,allow_null=False,allow_blank=False,max_length=2048)
    pic = serializers.ImageField(required=True,allow_null=True,allow_empty_file=True)

class deleteNewsSerializer(serializers.Serializer):
    news_id = serializers.CharField(required = True,allow_null=False,allow_blank=False,max_length=10)
