from django.urls import path
from .views import UserLoginView, UserRegisterView, RegistrationSucceedView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('register/succeed/', RegistrationSucceedView.as_view(), name='user_registration_succeed'),
]
