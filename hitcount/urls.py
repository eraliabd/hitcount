from django.urls import path
from .views import article, article_detail

urlpatterns = [
    path('', article, name='articles'),
    path('detail/<int:pk>/', article_detail, name='article_detail'),
]
