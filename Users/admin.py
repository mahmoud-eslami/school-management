from django.contrib import admin
from .models import  *

# this class make some field in django panel to show db information in better shape
class customUserProfile(admin.ModelAdmin):
    list_display = ['user','nationalCode','role','gender']

# register user profile model to show in django panel
admin.site.register(userProfile,customUserProfile)
