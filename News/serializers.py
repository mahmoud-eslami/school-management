from  rest_framework import serializers
from  django.contrib.auth.models import User

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