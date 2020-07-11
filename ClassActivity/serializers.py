from rest_framework import serializers
from .models import *


class LessonsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lessons
        fields = '__all__'

    def create(self, validated_data):
        return Lessons.objects.create(**validated_data)

    def update(self, instanse, validated_data):
        instanse.title = validated_data.get('title', instanse.title)
        instanse.section_id = validated_data.get(
            'section_id', instanse.section_id)
        instanse.save()
        return instanse


class WeeklyScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklySchedule
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        return WeeklySchedule.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.class_id = validated_data.get('class_id', instance.class_id)
        instance.week_day = validated_data.get('week_day', instance.week_day)
        instance.first_bell = validated_data.get(
            'first_bell', instance.first_bell)
        instance.second_bell = validated_data.get(
            'second_bell', instance.second_bell)
        instance.third_bell = validated_data.get(
            'third_bell', instance.third_bell)
        instance.forth_bell = validated_data.get(
            'forth_bell', instance.forth_bell)
        instance.fifth_bell = validated_data.get(
            'fifth_bell', instance.fifth_bell)
        instance.save()
        return instance
