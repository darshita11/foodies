"""foodies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
#same directory .
#different test.views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.indexdata),
    path('registration',views.registration),
    path('registrationdata',views.registrationdata),
    path('login',views.login),
    path('logindata',views.logindata),
    path('forgetpass',views.forgetpass),
    path('forgetdata',views.forgetdata),
    path('indexdata',views.indexdata),
    path('formelement',views.formelement,name='formelement'),
    path('formdataelement',views.formdataelement),
    path('showfooddetail',views.showfooddetail),
    path('adminedit',views.adminedit),
    path('update/<tid>',views.adminupdate),
    path('updatedata',views.updatedata,name='updatedata'),
    path('delete/<tid>',views.delete),
]
