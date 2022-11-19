from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('upload/', views.upload, name="UploadVideo"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register, name="register"),
    path('trending/', views.trending, name="trending"),
    re_path(r'^view/(?P<videoID>\d+)/$', views.video, name='ViewVideo')
]



