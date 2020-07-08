from rest_framework import serializers
from .models import *


class LessonsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'
        read_only_fields = ['id']

    def create(self , validated_data):
        return Lessons.objects.create(**validated_data)
