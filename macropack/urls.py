from django.contrib import admin
from django.urls import path
from .views import macropack

urlpatterns = [
    path('', macropack, name="macropack"),
]