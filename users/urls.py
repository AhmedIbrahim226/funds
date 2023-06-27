from django.urls import path
from .views import UserLoginView, UserRegisterView, RegistrationSucceedView

urlpatterns = [
    path("", UserLoginView.as_view(), name="login"),
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('register/succeed/', RegistrationSucceedView.as_view(), name='user_registration_succeed'),
]
