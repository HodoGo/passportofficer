"""PassportOfficer URL Configuration

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
from django.conf.urls import url
from django.urls import path,include
import django.contrib.auth.views
from datetime import datetime

import HouseApp.forms
import HouseApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', HouseApp.views.home, name='home'),
    path('report/',include('reportapp.urls')),
    url(r'^contact$', HouseApp.views.contact, name='contact'),
    url(r'^about$', HouseApp.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.LoginView,
        {
            'template_name': 'app/login.html',
            'authentication_form': HouseApp.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.LogoutView,
        {
            'next_page': '/',
        },
        name='logout'),
    #path('',include('HouseApp.urls'))
]
