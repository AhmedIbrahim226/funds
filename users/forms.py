from django.core.exceptions import ValidationError
from .fields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import UserAuth




class UserRegisterForm(UserCreationForm):
    phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='EG'), label=_('phone number'))
    class Meta:
        model = UserAuth
        fields = ('email', 'first_name', 'second_name', 'third_name', 'fourth_name', 'phone_number', 'password1', 'password2',)


class LoginForm(AuthenticationForm):
    username = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='EG'), required=False, label=_('phone number'))
    email = forms.EmailField(required=False, label=_('email'))

    def __init__(self, request, *args, **kwargs):
        super().__init__(request, *args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get("email")
        phone_number = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        auth = phone_number or email

        if auth is not None and password:
            self.user_cache = authenticate(
                self.request, username=auth, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


    def get_invalid_login_error(self):
        email = self.cleaned_data.get("email")

        return ValidationError(
            self.error_messages["invalid_login"],
            code="invalid_login",
            params={"username": _('email') if email else _('phone number')},
        )