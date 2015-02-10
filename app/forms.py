
from django import forms
import account.forms
from django.utils.translation import ugettext_lazy as _
from captcha.fields import CaptchaField
try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = None


class SignupForm(account.forms.SignupForm):

    name = forms.CharField(
            label=_("Name"),
            max_length=30,
            widget=forms.TextInput(), required=True
        )
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields["username"]
        field_order = ["email", "name", "password", "password_confirm", "captcha"]
        if not OrderedDict or hasattr(self.fields, "keyOrder"):
            self.fields.keyOrder = field_order
        else:
            self.fields = OrderedDict((k, self.fields[k]) for k in field_order)


class SignupInvForm(account.forms.SignupForm):

    name = forms.CharField(
            label=_("Name"),
            max_length=30,
            widget=forms.TextInput(), required=True
        )
    phone = forms.CharField(
            label=_("Phone"),
            max_length=30,
            widget=forms.TextInput(), required=True
        )
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super(SignupInvForm, self).__init__(*args, **kwargs)
        del self.fields["username"]
        field_order = ["email", "name", "phone", "password", "password_confirm", "captcha"]
        if not OrderedDict or hasattr(self.fields, "keyOrder"):
            self.fields.keyOrder = field_order
        else:
            self.fields = OrderedDict((k, self.fields[k]) for k in field_order)


class SignupInvPrecheckForm(forms.Form):

    company = forms.CharField(
        label=_("Company"),
        max_length=30,
        widget=forms.TextInput(), required=True
    )
    invite_code = forms.CharField(
        label=_("Invite code"),
        max_length=64,
        widget=forms.TextInput(), required=True
    )

    def clean(self):
        # TODO: check invite code
        return self.cleaned_data
