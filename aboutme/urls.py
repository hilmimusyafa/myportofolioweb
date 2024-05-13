from django.contrib import admin
from django.urls import path
from aboutme import views

urlpatterns = [
    path('', views.aboutme, name='aboutme'),
]
