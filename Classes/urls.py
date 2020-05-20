from django.urls import path, include
from . import views

urlpatterns = [
    path('get_all/classes/',views.GetAllClasses.as_view(),name='get_classes'),
]
