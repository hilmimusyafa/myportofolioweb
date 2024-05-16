from django.contrib import admin
from django.urls import path
from contact import views

urlpatterns = [
    path('', views.contact_view, name='contact'),
]