"""flashmob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from homeapp import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'about', views.about, name='about'),
    path(r'contact', views.contact, name='contact'),
    path(r'terms', views.terms, name='terms'),
    path(r'privacy', views.privacy, name='privacy'),
    path(r'modernmarket', views.modernmarket, name='modernmarket'),
    path(r'modernadvertising', views.modernadvertising, name='modernadvertising'),
    path(r'modernresearch', views.modernresearch, name='modernresearch'),
    path(r'moderncare', views.moderncare, name='moderncare'),
    path(r'modernengage', views.modernengage, name='modernengage'),
    path(r'integrationapis', views.integrationapis, name='integrationapis'),
    path(r'partner', views.partner, name='partner'),
    path(r'training', views.training, name='training'),
    path(r'agency', views.agency, name='agency'),
    path(r'customer', views.customer, name='customer'),
    path(r'', views.index, name='index'),
    path(r'', views.index, name='index'),
    path(r'', views.index, name='index'),
    path(r'', views.index, name='index'),
    path(r'', views.index, name='index'),
    path(r'', views.index, name='index'),
    path(r'', views.index, name='index'),
    path(r'', views.index, name='index'),

]
