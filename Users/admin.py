from django.contrib import admin
from .models import  *
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(userDoc)
class CustomDoc(admin.ModelAdmin):
    list_display=['user_id','personalCode','nationalCode','father_name','address','gender',]

@admin.register(Images)
class CustomImages(admin.ModelAdmin):
    list_display = ['id','user_id','image']

@admin.register(MyUser)
class CustomUser(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name','email')}),
        (_('Permissions'), {'fields': ('role','is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('id','username','email', 'first_name', 'last_name', 'is_staff','role','reset_code')
    search_fields = ('email', 'first_name', 'last_name')
