from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

class User(AbstractUser):

    username = models.CharField(
        error_messages={'unique': 'A user with that username already exists.'},
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        max_length=150,
        validators=[UnicodeUsernameValidator()],
        verbose_name='Nome'
    )

    email = models.EmailField(
        verbose_name='E-mail',
        max_length=255,
        unique=True,
    )


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"