from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

class User(AbstractUser):

    username = models.CharField(
        max_length=150,
        verbose_name='Apelido'
    )

    email = models.EmailField(
        verbose_name='Usuário(E-mail)',
        max_length=255,
        unique=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"