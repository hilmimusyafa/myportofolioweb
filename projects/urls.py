from django.contrib import admin
from django.urls import path
from projects import views
from projects.views import (
   MyProjectsListView, 
   MyProjectsDetailView,
)

# app_name = 'projects'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('/<str:slug>/', views.projects_detail, name='projects_detail'),
]
