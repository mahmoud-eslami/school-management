from django.contrib import admin
from .models import *


@admin.register(Lessons)
class CustomLessons(admin.ModelAdmin):
    list_display = ['id', 'title', 'section_id', ]


@admin.register(WeeklySchedule)
class CustomWeeklySchedule(admin.ModelAdmin):
    list_display = ['id', 'class_id', 'week_day', 'first_bell',
                    'second_bell', 'third_bell', 'forth_bell', 'fifth_bell']


@admin.register(PresentAbsentList)
class CustomPresentAbsentList(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'day', 'month', 'year']


@admin.register(GradeList)
class CustomGradeList(admin.ModelAdmin):
    list_display = ['id', 'grade_owner_id', 'teacher_id', 'lesson_id',
                    'grade_type', 'grade_count', 'day', 'month', 'year']
