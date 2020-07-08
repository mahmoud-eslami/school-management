from rest_framework import serializers
from .models import *


class LessonsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        return Lessons.objects.create(**validated_data)

    def update(self, instanse, validated_data):
        instanse.title = validated_data.get('title', instanse.title)
        instanse.section_id = validated_data.get(
            'section_id', instanse.section_id)
        instanse.save()
        return instanse
