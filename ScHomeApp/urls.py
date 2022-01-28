from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.SiteHome,name='sitehome'),
    path('schome',views.ScHome,name='schome')
]