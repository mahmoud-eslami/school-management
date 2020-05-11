from django.contrib import admin
from .models import *

@admin.register(News)
class CustomNews(admin.ModelAdmin):
    list_display = ['id','title','release_date']
