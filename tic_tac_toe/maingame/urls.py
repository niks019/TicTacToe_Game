from django.contrib import admin
from django.urls import path, include
from maingame import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('play', views.play, name='play'),
    path('feed-back', views.feedback, name='feedback'),
    path('asubmit', views.asubmit, name='asubmit')
]
