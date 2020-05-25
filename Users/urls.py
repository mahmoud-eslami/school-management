from django.urls import path, include
from  . import views

urlpatterns = [
    path('user/profile/',views.userProfileApi.as_view(),name='user_profile'),
    path('user/UpdateUserAndUserDoc/',views.UpdateUserAndUserDoc.as_view(),name='update_user_userDoc'),
    path('user/ChangePassInProfile/',views.ChangePassInProfile.as_view(),name='change_pass_profile'),
    path('user/GetAllUserInfo/',views.GetAllUserInfo.as_view(),name='get_all_user_info'),
    path('userDoc/api/',views.UserDocApi.as_view(),name='user_doc'),
    path('user/api/',views.UserApi.as_view(),name='user'),
    path('images/api/',views.ImageApi.as_view(),name='image'),
    path('regiseter_user/',views.registerUserApi.as_view(),name='register_user'),
    
]
