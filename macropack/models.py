from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, Permission, Group
)
from django.utils.translation import gettext as _


class PermissoesMacropack(models.Model):

    class Meta:

        managed = True

        permissions = (
            ('macropack_permissoes', 'Permissão Global de Macropack'),
        )

        verbose_name = "Permissão"
        verbose_name_plural = "Permissões"


# class CustomPermissionsMixin(models.Model):
#     """
#     A mixin class that adds the fields and methods necessary to support
#     Django's Group and Permission model using the ModelBackend.
#     """
#     is_superuser = models.BooleanField(
#         _('superuser status'),
#         default=False,
#         help_text=_(
#             'Designates that this user has all permissions without '
#             'explicitly assigning them.'
#         ),
#     )
#     groups = models.ManyToManyField(
#         Group,
#         verbose_name=_('groups'),
#         blank=True,
#         help_text=_(
#             'The groups this user belongs to. A user will get all permissions '
#             'granted to each of their groups.'
#         ),
#         related_name="MacropackUser_set",
#         related_query_name="MacropackUser",
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         verbose_name=_('Permissões Macropack'),
#         blank=True,
#         help_text=_('Specific permissions for this user.'),
#         related_name="MacropackUser_set",
#         related_query_name="MacropackUser",
#     )

#     class Meta:
#         abstract = True
#
# class MacropackUserManager(BaseUserManager):
#     def create_user(self, email, name, password=None):
#         """
#         Creates and saves a User with the given email, date of
#         birth and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         user = self.model(
#             email=self.normalize_email(email),
#             name=name,
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, name, password):
#         """
#         Creates and saves a superuser with the given email, date of
#         birth and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#             name=name,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
#
#
# class MacropackUser(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name='Usuário(E-mail)',
#         max_length=255,
#         unique=True,
#         blank=False,
#         null=False,
#     )
#
#     # groups = models.ManyToManyField(
#     #     blank=True,
#     #     help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
#     #     related_name='MacropackUser.groups+', related_query_name='macropackuser', to='auth.Group',
#     #     verbose_name='Grupos'
#     # )
#     #
#     # user_permissions = models.ManyToManyField(
#     #     blank=True,
#     #     help_text='Especifica permissões para este usuário',
#     #     related_name='MacropackUser.user_permissions+',
#     #     related_query_name='macropackuser', to='auth.Permission', verbose_name='Permissões de Usuários'
#     # )
#
#     name = models.CharField(verbose_name="Apelido", max_length=150, blank=False, null=False)
#     is_active = models.BooleanField(verbose_name="Ativo", default=True)
#     is_admin = models.BooleanField(verbose_name="Administrador", default=False)
#
#     objects = MacropackUserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']
#
#     def __str__(self):
#         return self.email
#
#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True
#
#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True
#
#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         # Simplest possible answer: All admins are staff
#         return self.is_admin
#
#
#     class Meta:
#         verbose_name = "Usuário"
#         verbose_name_plural = "Usuários"
#
#         permissions = (
#             ('pode_adicionar_macropackuser', 'Pode adicionar Macropack User'),
#         )