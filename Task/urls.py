"""Task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from Taskapp.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index,name="index"),
    url(r'^index/$',index,name="index"),
    url(r'^login/$',login,name="login"),
    url(r'^regaction/$',regaction,name="regaction"),
    url(r'^register/$',register,name="register"),
    url(r'^logaction/$',logaction,name="logaction"),
    url(r'^welcome/$',welcome,name="welcome"),
    url(r'^pinformation/$',pinformation,name="pinformation"),
    url(r'^paction/$',paction,name="paction"),
    
    
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)