from django.contrib import admin
from django.urls import path
from .views import contas, logout_sistema
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', contas, name="contas"),
    path('entrar/', LoginView.as_view(template_name='login.html'), name="login"),
    path('sair/', logout_sistema, name="logout"),
]