from django.urls import path, include
from . import views

urlpatterns = [
    path('lessons/Api/', views.lessonsApi.as_view(), name='lesson_api'),
    path('lessons/GetAllLesson/',
         views.GetAllLessons.as_view(), name='get_all_lesson'),
    path('weeklySchedule/Api', views.weeklyScheduleApi.as_view(),
         name='weekly_schedule_api'),
    path('weeklySchedule/GetClassSchedule/',
         views.getClassWeeklySchedule.as_view(), name='get_class_weekly_schedule'),
    path('lessons/GetLessonsBySection/',views.getLessonsBySection.as_view(),name='get_lessons_section'),
    path('presentAbsentList/Api/',views.PersentAbsentApi.as_view(),name='present_absent_list'),
]
