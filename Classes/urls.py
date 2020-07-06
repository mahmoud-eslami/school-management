from django.urls import path, include
from . import views

urlpatterns = [
    path('get_all/classes/',views.GetAllClasses.as_view(),name='get_classes'),
    path('get_all/user_class/',views.GetAllUserClasses.as_view(),name='get_user_class'),
]
