from django.contrib import admin
from django.urls import path , include
from MyWeatherApp import views
urlpatterns = [
    path("",views.home,name='home'),
    
]
