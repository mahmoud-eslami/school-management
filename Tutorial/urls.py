from django.urls import path,include
from . import *
from . import views
from rest_framework.compat import path


urlpatterns = [
    path('tutorial/api/', views.tutorialApi.as_view(), name='tutorial'),
    path('tutorial/api/upload/', views.FileUploadView.as_view() , name = 'upload_tutorial'),
    path('tutorial/api/all_tutorial/', views.getAlltutorial.as_view() , name = 'all_tutorial'),
]
