from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)