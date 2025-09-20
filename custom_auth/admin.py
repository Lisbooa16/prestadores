from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from custom_auth.models.permissoes import ApiPermission
from .models import CustomUser
from .forms import ApiPermissionForm, CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "nome", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    ordering = ("email",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                    "nome",
                    "username",
                    "telefone",
                    "prestador",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "nome",
                    "telefone",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )


class ApiPermissionAdmin(admin.ModelAdmin):
    form = ApiPermissionForm
    list_display = ("user", "method", "route", "can_access")
    list_filter = ("method", "can_access")
    search_fields = ("user__username", "user__email", "route")


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ApiPermission, ApiPermissionAdmin)
