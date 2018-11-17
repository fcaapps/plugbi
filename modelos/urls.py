
from django.contrib import admin
from django.urls import path
from .views import modelos, politica

urlpatterns = [
    path('', modelos, name="modelos"),
    path('politica-privacidade', politica, name="politica"),
]