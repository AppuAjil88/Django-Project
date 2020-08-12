from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.pdf_list, name='pdf_list'),
    path('upload/', views.pdf_upload, name='pdf_upload'),
]
