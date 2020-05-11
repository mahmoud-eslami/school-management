from django.contrib import admin
from .models import *

# new annotaition use instead of admin.site.register
############################
@admin.register(News)
############################
class CustomNews(admin.ModelAdmin):
    list_display = ['id','title','release_date','author_id']
