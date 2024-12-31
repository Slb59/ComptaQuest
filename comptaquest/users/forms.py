from django import forms
from django.contrib.auth import forms as auth_forms

from .models import CQUser, MemberProfile


class CQUserCreationForm(auth_forms.UserCreationForm):
    """New Member Creation Form"""

    class Meta(auth_forms.UserCreationForm):
        model = CQUser
        fields = {"trigram", "email", "password"}


class CQUserChangeForm(auth_forms.UserChangeForm):
    """New Member Creation Form"""

    class Meta(auth_forms.UserCreationForm):
        model = CQUser
        fields = {"trigram", "email", "password"}
