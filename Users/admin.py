from django.contrib import admin
from .models import  *
from django.contrib.auth.admin import User


@admin.register(userDoc)
class CustomDoc(admin.ModelAdmin):
    list_display=['user_id','personalCode','nationalCode','father_name','address','gender','role']

@admin.register(Images)
class CustomImages(admin.ModelAdmin):
    list_display = ['user_id','image']
