import djano.urls import path,include
from . import *


urlpatterns = [
    path('tutorial/api/', views.tutorialApi.as_view(), name='tutorial')
]
