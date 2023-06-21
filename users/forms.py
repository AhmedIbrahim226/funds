from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django import forms


class LoginForm(AuthenticationForm):
    phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='EG'), required=False)
    email = forms.EmailField(required=False)

    def __init__(self, request, *args, **kwargs):
        super().__init__(request, *args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get("email")
        phone_number = self.cleaned_data.get("phone_number")
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