from django.urls import path
from api.views import ArticleAPIView

urlpatterns = [
    path('articles_info/', ArticleAPIView.as_view(), name='articles-info'),
]