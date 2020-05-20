from django.contrib import admin

@admin.register(Classes)
class CustomClasses(admin.ModelAdmin):
    list_display=['user_id','name','id']
