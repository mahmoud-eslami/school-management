from django.urls import path, include
from  . import views

urlpatterns = [
    path('get/all_user/',views.getAllUser.as_view(),name='getAllUser'),
    path('delete_user/by_id/',views.deleteUser.as_view(),name='deleteUser'),
    path('regiseter_user/',views.registerUser.as_view(),name='registerUser'),
    path('find_user/by_id/',views.findUserById.as_view(),name='findUserById'),
    path('find_user/by_username/',views.findUserByUsername.as_view(),name='findUserByUsername'),
    path('edit_user/by_id/',views.editSpecificUser.as_view(),name='editSpecificUser'),
    path('edit_userProfile/by_id/',views.editSpecificUserProfile.as_view(),name='editSpecificUserProfile'),
    path('edit_userDoc/by_id/',views.editSpecificUserDoc.as_view(),name='editSpecificUserDoc'),
]
