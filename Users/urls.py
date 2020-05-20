from django.urls import path, include
from  . import views

urlpatterns = [
    path('user/profile/',views.userProfileApi.as_view(),name='user_profile'),
    path('userDoc/api/',views.UserDocApi.as_view(),name='user_doc'),
    path('user/api/',views.UserApi.as_view(),name='user'),
    path('images/api/',views.ImageApi.as_view(),name='image'),
    path('regiseter_user/',views.registerUserApi.as_view(),name='register_user'),
    
]
