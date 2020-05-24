from  rest_framework import serializers
from  django.contrib.auth.models import User
from datetime import datetime
from .models import *
from school.validators import validate_image_size
from Users.serializers import *

class NewsSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = News
        fields = '__all__'

    def create(self , validated_data):
        return News.objects.create(**validated_data)

    def update(self ,instance , validated_data):
        instance.title = validated_data.get('title' , instance.title)
        instance.content = validated_data.get('content' , instance.content)
        instance.pic = validated_data.get('pic' , instance.pic)
        instance.release_date = validated_data.get('release_date' , instance.release_date)
        instance.save()
        return instance
