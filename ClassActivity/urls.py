from django.urls import path, include
from . import views

urlpatterns = [
    path('lessons/Api/', views.lessonsApi.as_view(), name='lesson_api'),
    path('lessons/GetAllLesson/',
         views.GetAllLessons.as_view(), name='get_all_lesson'),
    path('weeklySchedule/Api', views.weeklyScheduleApi.as_view(),
         name='weekly_schedule_api')
]
