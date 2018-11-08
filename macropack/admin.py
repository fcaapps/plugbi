from django.contrib import admin
from .models import PermissoesMacropack

admin.site.register(PermissoesMacropack)

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#
# from .models import MacropackUser
# from .models import PermissoesMacropack
# from .forms import UserCreationForm, UserChangeForm
#
# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     form = UserChangeForm
#     add_form = UserCreationForm
#
#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('email', 'name', 'is_admin')
#     list_filter = ('is_admin',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Informações Pessoais', {'fields': ('name',)}),
#         ('Permissões', {'fields': ('is_active', 'is_admin', 'is_superuser', 'user_permissions')}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'name', 'password1', 'password2')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()
#
#     # def has_change_permission(self, request, obj=None):
#     #     has_class_permission = super(UserAdmin, self).has_change_permission(request, obj)
#     #     if not has_class_permission:
#     #         return False
#     #     # if obj is not None and not request.user.is_superuser:
#     #     #     return False
#     #     # return True
#     #
#     # def queryset(self, request):
#     #     if request.user.is_superuser:
#     #         return MacropackUser.objects.all()
#     #     return MacropackUser.objects.filter(email=request.user)
#     #
#     # def save_model(self, request, obj, form, change):
#     #     if not change:
#     #         obj.author = request.user
#     #     obj.save()
#
# # Now register the new UserAdmin...
# admin.site.register(MacropackUser, UserAdmin)