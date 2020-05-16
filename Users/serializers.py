from rest_framework import serializers
from .models import *

class ImageSerilizer(serializers.Serializer):
    user_id = serializers.CharField(max_length=3,allow_blank=False,allow_null=True)
    image = serializers.ImageField(max_length=None, allow_empty_file=False,)

    def create(self , validated_data):
        return Images.objects.create(**validated_data)

    def update(self , instance , validated_data):
        instance.image = validated_data.get('image' , instance.image)
        instance.save()
        return instance

class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True,max_length=5)
    username = serializers.CharField(read_only=True,allow_null=False,allow_blank=True,max_length=20)
    first_name = serializers.CharField(allow_null=False,allow_blank=True,max_length=20)
    last_name = serializers.CharField(allow_null=False,allow_blank=True,max_length=20)
    email = serializers.EmailField(allow_null=False,allow_blank=True,max_length=20)
    date_joined = serializers.DateTimeField(read_only=True)

    def create(self , validated_data):
        return User.objects.create(**validated_data)

    def update(self , instance , validated_data):
        instance.first_name = validated_data.get('first_name' , instance.first_name)
        instance.last_name = validated_data.get('last_name' , instance.last_name)
        instance.email = validated_data.get('email' , instance.email)
        instance.save()
        return instance


class UserDocSerializer(serializers.Serializer):
    user_id = serializers.CharField(read_only=True)
    role = serializers.ChoiceField(choices=role_choices,default=STUDENT)
    uuid = serializers.UUIDField()
    religon = serializers.CharField(max_length=40,allow_blank=True,allow_null=True)
    userPhoto = serializers.CharField(max_length=250,allow_blank=True,allow_null=True)
    userNationalCardPhoto = serializers.CharField(max_length=250,allow_blank=True,allow_null=True)
    userIdCardPhoto = serializers.CharField(max_length=250,allow_blank=True,allow_null=True)
    user_pNum = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    home_pNum = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    address = serializers.CharField(max_length=250,allow_null=True,allow_blank=False)
    zipCode = serializers.CharField(max_length=20,allow_blank=False,allow_null=True)
    personalCode = serializers.CharField(max_length=20,allow_null=True,allow_blank=True)
    nationalCode = serializers.CharField(max_length=20,allow_blank=False,allow_null=True)
    father_nationalCode = serializers.CharField(max_length=20,allow_blank=False,allow_null=True)
    father_name = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    father_pNum = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    father_jobName = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    father_jobAddress = serializers.CharField(max_length=250,allow_null=True,allow_blank=False)
    father_job_pNum = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    mother_nationalCode = serializers.CharField(max_length=20,allow_blank=False,allow_null=True)
    mother_name = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    mother_pNum = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    mother_jobName = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    mother_jobAddress = serializers.CharField(max_length=250,allow_null=True,allow_blank=False)
    mother_job_pNum = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    citizen_Num = serializers.CharField(max_length=40,allow_blank=True,allow_null=True)
    date_of_birth = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    place_of_birth = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    citizen = serializers.ChoiceField(choices=citizen_choices,default=IRAN)
    gender = serializers.ChoiceField(choices=gender_choices,default=MAN)
    section = serializers.ChoiceField(choices=section_choices,default=pre_one)
