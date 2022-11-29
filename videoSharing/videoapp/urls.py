from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('upload/', views.upload, name="UploadVideo"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register, name="register"),
    path('trending/', views.trending, name="trending"),
    re_path(r'^view/(?P<videoID>\d+)/$', views.video, name='ViewVideo')
]



