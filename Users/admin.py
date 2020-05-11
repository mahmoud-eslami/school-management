from django.contrib import admin
from .models import  *
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class userProfileInLine(admin.StackedInline):
    model = userProfile
    can_delete = False


class userDocInLine(admin.StackedInline):
    model = userDoc
    can_delete = False

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    field_set = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_field = (
            (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
                }),
    )
    list_display = ('email' , 'first_name' , 'last_name' , 'is_staff' , 'username')
    search_field = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    inlines = (userProfileInLine,userDocInLine)
