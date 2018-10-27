from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as UserBaseAdmin
from .models import User

class UserAdmin(UserBaseAdmin):
    list_display = ('email', 'username')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_active','is_staff', 'is_superuser', 'user_permissions')}),
    )

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)