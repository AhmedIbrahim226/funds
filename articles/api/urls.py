from django.urls import path
from .views import ArticleApiView

urlpatterns = [
    path("", ArticleApiView.as_view({'get': 'list', 'post': 'create'})),
]