from django.urls import path, include
from  . import views

urlpatterns = [
    path('lessons/Api/',views.lessonsApi.as_view(),name='lesson_api'),
]