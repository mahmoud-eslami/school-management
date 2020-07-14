from rest_framework import serializers
from .models import *

class CustomUsersOfClassSerializer(serializers.Serializer):
    user_id = serializers.CharField(read_only=True)

class ClassSerializer(serializers.ModelSerializer):

    section_id = serializers.CharField(
        max_length=2, allow_null=False, allow_blank=False)

    class Meta:
        model = Classes
        fields = '__all__'
        # read_only_field = ['id'] #### PK set read only as default

    def create(self, validated_data):
        return Classes.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.section_id = validated_data.get(
            'section_id', instance.section_id)
        instance.save()
        return instance


class UserClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClass
        fields = '__all__'

    def create(self , validated_data):
        return UserClass.objects.create(**validated_data)