from django.contrib import admin
from .models import  *

@admin.register(Tutorial)
class CustomToturial(admin.ModelAdmin):
    list_display=['id','title','ttype','tfile','writer']

@admin.register(file)
class CustomFile(admin.ModelAdmin):
    list_display=['user_id','file']
