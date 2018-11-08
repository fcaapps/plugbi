from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as UserBaseAdmin
from .models import User


class FilterUserAdmin(UserBaseAdmin):
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

    def get_queryset(self, request):
        # For Django < 1.6, override queryset instead of get_queryset
        qs = super(FilterUserAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    # def has_change_permission(self, request, obj=None):
    #     if not obj:
    #         # the changelist itself
    #         return True
    #     return obj.user == request.user

class UserAdmin(FilterUserAdmin):
    list_display = ('email', 'username')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('username',)}),
        ('Permissões', {'fields': ('is_active','is_staff', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
         ),
    )

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)