<<<<<<< HEAD
"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from Token.views import CustomTokenObtainPairView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # access to jet dashboard
    #path('jet/',include('jet.urls','jet')),
    #path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    #==============================================
    path('admin/', admin.site.urls),
    #==============================================
    # this urls route you to Users app urls.py
    path('Users/App/' , include('Users.urls')),
    #==============================================
    # this urls route you to Users app urls.py
    path('News/App/' , include('News.urls')),
    #==============================================
    # this urls route you to Users app urls.py
    path('Classes/App/' , include('Classes.urls')),
    #==============================================
    #==============================================
    # this urls route you to Tutorial app urls.py
    path('Tutorial/App/' , include('Tutorial.urls')),
    #==============================================
    # token urls
    path('api/login/',CustomTokenObtainPairView.as_view(),name='TokenObtainPairView'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='TokenRefreshView'),
    #==============================================
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from Token.views import CustomTokenObtainPairView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # access to jet dashboard
    #path('jet/',include('jet.urls','jet')),
    #path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    #==============================================
    path('admin/', admin.site.urls),
    #==============================================
    # this urls route you to Users app urls.py
    path('Users/App/' , include('Users.urls')),
    #==============================================
    # this urls route you to Users app urls.py
    path('News/App/' , include('News.urls')),
    #==============================================
    # this urls route you to Users app urls.py
    path('Classes/App/' , include('Classes.urls')),
    #==============================================
    #==============================================
    # this urls route you to Tutorial app urls.py
    path('Tutorial/App/' , include('tutorial.urls')),
    #==============================================
    # token urls
    path('api/login/',CustomTokenObtainPairView.as_view(),name='TokenObtainPairView'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='TokenRefreshView'),
    #==============================================
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> dd13af56e1140249d9736fa2532530f84604ca64
