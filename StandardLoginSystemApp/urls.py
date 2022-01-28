from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('slshome',views.SLShome,name='slshome'),
    path('login',views.Login,name='login'),
    path('signup',views.SignUp,name='signup'),
    path('verify/<uidb64>/<token>',views.Verify,name='verify'),
    path('logout',views.Logout,name='logout'),
]