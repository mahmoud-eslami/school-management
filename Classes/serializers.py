from rest_framework import serializers
from .models import *


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'
        #read_only_field = ['id'] #### PK set read only as default
    def create(self , validated_data):
        return Classes.objects.create(**validated_data)

    def update(self , instance , validated_data):
        instance.name = validated_data.get('name' ,instance.name)
        instance.save()
        return instance

class UserClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClass
        fields = '__all__'
