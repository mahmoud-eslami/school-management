from rest_framework import serializers
from .models import *
from school.validators import *
from Users.serializers import UserSerializer

class TutorialSerilizer(serializers.Serializer):
    writer = UserSerializer(read_only=True)
    id = serializers.CharField(max_length=10,read_only=True)
    writer_id = serializers.CharField(max_length=10,allow_null=False,allow_blank=True)
    title = serializers.CharField(max_length=250,allow_null=False,allow_blank=False)
    content = serializers.CharField(max_length=250,allow_null=False,allow_blank=False)
    release_date = serializers.CharField(max_length=100,allow_null=False,allow_blank=False)
    tfile = serializers.CharField(max_length=250,allow_null=True,allow_blank=True)

    def create(self , validated_data):
        return Tutorial.objects.create(**validated_data)

    def update(self , instance , validated_data):
        instance.title = validated_data.get('title' , instance.title)
        instance.content = validated_data.get('content' , instance.content)
        instance.tfile = validated_data.get('tfile' , instance.tfile)
        instance.save()
        return instance

class UploadFileSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=3,allow_blank=True,allow_null=False)
    file = serializers.FileField(max_length=None, allow_empty_file=False,use_url=True,validators=[validate_file_size,validate_format_file])

    def create(self,validated_data):
        return File.objects.create(**validated_data)
