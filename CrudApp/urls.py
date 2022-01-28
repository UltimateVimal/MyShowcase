from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('crudhome',views.CrudHome,name='crudhome'),
    path('addstudent',views.AddStudent,name='AddStudent'),
    path('displayall',views.DisplayAll,name='displayall'),
    path('deletestudent',views.DeleteStudent,name='deletestudent'),
]