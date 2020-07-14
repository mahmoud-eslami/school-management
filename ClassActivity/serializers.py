from rest_framework import serializers
from .models import *


class GradeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = GradeList
        fields = '__all__'

    def create(self , validated_data):
        return GradeList.objects.create(**validated_data)    

    def update(self , instance, validated_data):
        instance.grade_owner_id = validated_data.get('grade_owner_id',instance.grade_owner_id)
        instance.teacher_id = validated_data.get('teacher_id', instance.teacher_id)
        instance.lesson_id = validated_data.get('lesson_id', instance.lesson_id)
        instance.grade_type = validated_data.get('grade_type', instance.grade_type)
        instance.grade_count = validated_data.get('grade_count', instance.grade_count)
        instance.day = validated_data.get('day', instance.day)
        instance.month = validated_data.get('month', instance.month)
        instance.year = validated_data.get('year', instance.year)
        instance.save()
        return instance



class PresentAbsentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PresentAbsentList
        fields = ['user_id','day','month','year']

    def create(self, validated_data):
        return PresentAbsentList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.day = validated_data.get('day', instance.day)
        instance.month = validated_data.get('month', instance.month)
        instance.year = validated_data.get('year', instance.year)
        instance.save()
        return instance


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
