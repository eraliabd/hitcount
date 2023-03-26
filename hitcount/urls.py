from django.urls import path
from .views import article, article_detail, ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='articles'),
    # path('', article, name='articles'),
    path('detail/<int:pk>/', article_detail, name='article_detail'),
]
