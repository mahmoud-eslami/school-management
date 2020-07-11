from django.urls import path, include
from . import views

urlpatterns = [
    path('get_all/classes/',views.GetAllClasses.as_view(),name='get_classes'),
    path('get_all/user_class/',views.GetAllUserClasses.as_view(),name='get_user_class'),
    path('classes/Api/',views.ClassesApi.as_view(),name='class_api'),
    path('userClasses/Api/',views.userClassesApi.as_view(),name='user_Classes'),
]
