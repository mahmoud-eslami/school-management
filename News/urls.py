from  django.urls import path, include
from . import views

urlpatterns = [
    path('api/',views.NewsApi.as_view(),name='newsApi'),
    path('news/GetAllNewsInfo/',views.GetAllNewsInfo.as_view(),name='get_all_news'),
]
