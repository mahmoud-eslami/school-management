from django.urls import path, include
from  . import views

urlpatterns = [
    path('user/api/',views.UserApi.as_view(),name='user_api'),
    path('images/api/',views.ImageApi.as_view(),name='image_api'),
    path('regiseter_user/',views.registerUser.as_view(),name='registerUser'),
]
