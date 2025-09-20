from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from custom_auth.models.permissoes import ApiPermission, get_all_routes
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("email", "nome", "telefone")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email", "nome", "telefone", "is_active", "is_staff")


class ApiPermissionForm(forms.ModelForm):
    class Meta:
        model = ApiPermission
        fields = "__all__"

    route = forms.ChoiceField(choices=get_all_routes)
