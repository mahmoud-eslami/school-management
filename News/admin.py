from django.contrib import admin
from .models import *

# new annotaition use instead of admin.site.register
############################
@admin.register(News)

