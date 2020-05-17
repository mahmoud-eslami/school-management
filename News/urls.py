from  django.urls import path, include
from . import views

urlpatterns = [
    path('api/',views.NewsApi.as_view(),name='newsApi')
]
