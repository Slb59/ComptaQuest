from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms

from .models import MemberProfile

User = get_user_model()

class UserCreationForm(auth_forms.UserCreationForm):
    """ New Member Creation Form """

    class Meta(auth_forms.UserCreationForm):
        model = User
        fields = {"trigram", "username", "email", "password"}
