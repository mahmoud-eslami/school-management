from django.urls import path, include
from  . import views

urlpatterns = [
    path('get/all_user/',views.getAllUser.as_view(),name='getAllUser'),
    path('delete_user/username/',views.deleteUser.as_view(),name='deleteUser'),
]
