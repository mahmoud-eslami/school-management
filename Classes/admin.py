from django.contrib import admin
from .models import *

@admin.register(Classes)
class CustomClasses(admin.ModelAdmin):
    list_display=['name','id']

@admin.register(UserClass)
class CustomClasses(admin.ModelAdmin):
    list_display=['user_id','userClass_id']