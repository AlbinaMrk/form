from django.contrib import admin
from django.urls import path, include
from .views import page1

urlpatterns = [
    path('',page1),

]
