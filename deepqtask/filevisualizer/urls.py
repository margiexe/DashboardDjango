# filevisualizer/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.visualize_data, name='visualize_data'),
]
