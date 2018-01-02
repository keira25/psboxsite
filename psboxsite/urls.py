"""psboxsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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


urlpatterns = [
    path('nimda/', admin.site.urls),
    path('', views.home_view.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('accounts/signup/', views.signup_view.as_view(), name='signup'),
    path('accounts/login/', views.login_view.as_view(), name='login'),       
    path('projects/', include('projects.urls')),      
    
]
