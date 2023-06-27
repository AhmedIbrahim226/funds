"""
URL configuration for funds project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_protect, csrf_exempt, ensure_csrf_cookie

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self, attrs):
        user = authenticate(username=attrs['username'],
        password=attrs['password'])
        if not user:
            raise serializers.ValidationError('Incorrect username or password.')
        if not user.is_active:
            raise serializers.ValidationError('User is disabled.')
        return {'user': user}

csrf_protect_method = method_decorator(csrf_exempt)
class LoginView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()
    @csrf_protect_method
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response("Logged in")



"""
"""
ensure_csrf = method_decorator(ensure_csrf_cookie)
class setCSRFCookie(APIView):
    permission_classes = []
    authentication_classes = []
    @ensure_csrf
    def get(self, request):
        return Response("CSRF Cookie set.")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/setcsrf/', setCSRFCookie.as_view()),
    path('api/login/', LoginView.as_view()),
    path('', include('users.urls')),
    path('articles/', include('articles.urls')),
    path('api/articles/', include('articles.api.urls')),
]
