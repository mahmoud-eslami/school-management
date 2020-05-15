from rest_framework import serializers
from .models import *

class User(serializers.Serializer):
    id = serializers.CharField(read_only=True,max_length=5)
    username = serializers.CharField(allow_null=False,allow_blank=True,max_length=5)
    first_name = serializers.CharField(allow_null=False,allow_blank=True,max_length=5)
    last_name = serializers.CharField(allow_null=False,allow_blank=True,max_length=5)
    email = serializers.EmailField(allow_null=False,allow_blank=True,max_length=5)
    date_joined = serializers.DateTimeField()

    def create(self , validated_data):
        return User.objects.create(**validated_data)

    def update(self , instance , validated_data):
        instance.username = validated_data.get('username' , instance.username)
        instance.first_name = validated_data.get('first_name' , instance.first_name)
        instance.last_name = validated_data.get('last_name' , instance.last_name)
        instance.email = validated_data.get('email' , instance.email)
        instance.date_joined = validated_data.get('date_joined' , instance.date_joined)
        instance.save()
        return instance


class UserDoc(serializers.Serializer):
    user_id = serializers.CharField(read_only=True)
    role = serializers.ChoiceField(choices=role_choices,default=STUDENT)
    uuid = serializers.UUIDField()
    userPhoto = serializers.ImageField()
    nationalCardPhoto = serializers.ImageField()
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
    date_of_birth = serializers.DateTimeField()
    place_of_birth = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    citizen = serializers.ChoiceField(choices=citizen_choices,default=IRAN)
    gender = serializers.ChoiceField(choices=gender_choices,default=MAN)
    section = serializers.ChoiceField(choices=section_choices,default=pre_one)
