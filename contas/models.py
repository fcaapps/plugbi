from django.db import models
from django.contrib.auth.models import AbstractUser

class PermissoesContas(models.Model):

    class Meta:

        managed = False

        permissions = (
            ('contas_permissoes', 'Permissão Global de Contas'),
        )

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

    author = models.ForeignKey('contas.User', verbose_name='Autor', null=True, blank=True, on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"