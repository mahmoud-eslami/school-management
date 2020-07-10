from django.contrib import admin
from .models import *

@admin.register(Lessons)
class CustomLessons(admin.ModelAdmin):
    list_display=['id','title','section_id',]

@admin.register(WeeklySchedule)
class CustomWeeklySchedule(admin.ModelAdmin):
    list_display=['id','class_id','week_day','first_bell','second_bell'
    ,'third_bell','forth_bell','fifth_bell']