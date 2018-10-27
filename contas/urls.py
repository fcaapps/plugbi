from django.contrib import admin
from django.urls import path
from .views import contas

urlpatterns = [
    path('', contas, name="contas"),
]