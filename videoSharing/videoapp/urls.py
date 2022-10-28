from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('upload/', views.upload, name="UploadVideo"),
    path('login/', views.upload, name="login"),
]

