from django.shortcuts import render
from django.urls import path
from .views import Demo

urlpatterns = [
    path('', Demo.as_view(), name="home"),
]