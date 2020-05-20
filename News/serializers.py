from  rest_framework import serializers
from  django.contrib.auth.models import User
from datetime import datetime
from .models import *
from school.validators import validate_image_size

class NewsSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True,allow_null=True,allow_blank=True,max_length=10)
    title = serializers.CharField(max_length=20,allow_blank=False,allow_null=True)
    content = serializers.CharField(max_length=200,allow_blank=False,allow_null=True)
    author_id = serializers.CharField(allow_null=False,allow_blank=True,max_length=10)
    pic = serializers.ImageField(max_length=None, allow_empty_file=False,use_url=True,validators=[validate_image_size,])
    release_date = serializers.DateTimeField(read_only=True)

    def create(self , validated_data):
        return News.objects.create(**validated_data)

    def update(self ,instance , validated_data):
        instance.title = validated_data.get('title' , instance.title)
        instance.content = validated_data.get('content' , instance.content)
        instance.pic = validated_data.get('title' , instance.pic)
        instance.save()
        return instance
