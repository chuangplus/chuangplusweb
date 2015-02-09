
from django import forms
import account.forms
from django.utils.translation import ugettext_lazy as _
from app.models import *


class SignupForm(account.forms.SignupForm):

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields["username"]
        del self.fields["password"]
        del self.fields["password_confirm"]
        del self.fields["email"]
        del self.fields["code"]
        self.email = forms.EmailField(
            label=_("Email"),
            widget=forms.TextInput(), required=True
        )
        self.name = forms.CharField(
            label=_("Name"),
            max_length=30,
            widget=forms.TextInput(), required=True
        )
        self.password = forms.CharField(
            label=_("Password"),
            widget=forms.PasswordInput(render_value=False)
        )
        self.password_confirm = forms.CharField(
            label=_("Password (again)"),
            widget=forms.PasswordInput(render_value=False)
        )
        self.code = forms.CharField(
            max_length=64,
            required=False,
            widget=forms.HiddenInput()
        )
        self.fields["email"] = self.email
        self.fields["name"] = self.name
        self.fields["password"] = self.password
        self.fields["password_confirm"] = self.password_confirm
        self.fields["code"] = self.code