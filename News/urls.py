from  django.urls import path, include
from . import views

urlpatterns = [
    path('get/all_news/',views.allNews.as_view(),name='allNews'),
    path('add_news/',views.addNews.as_view(),name='addNews'),
    path('delete_news/',views.deleteNews.as_view(),name='deleteNews'),
    path('edit_news/',views.editNews.as_view(),name='editNews'),
]
