from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutme', views.aboutme, name='aboutme'),
    path('contacts', views.contact_view, name='contact'),
    path('projects', views.projects, name='projects'),
    path('projects/<str:slug>/', views.projects_detail, name='projects_detail'),
]
