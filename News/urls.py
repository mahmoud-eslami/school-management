from  django.urls import path, include
from . import views

urlpatterns = [
    path('get/all_news/',views.allNews.as_view(),name='allNews'),
    path('add_news/',views.addNews.as_view(),name='addNews'),
]
