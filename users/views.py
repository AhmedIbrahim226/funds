from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView

from .forms import LoginForm, UserRegisterForm
from django.shortcuts import resolve_url

class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def get_default_redirect_url(self):
        if self.next_page:
            return resolve_url(self.next_page)
        else:
            return resolve_url('/articles/dashboard/')



class UserRegisterView(CreateView, FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('user_registration_succeed')


class RegistrationSucceedView(TemplateView):
    template_name = 'users/registration_succeed.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


