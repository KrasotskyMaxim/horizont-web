from drfasyncview import AsyncAPIView
from django.http import JsonResponse

from rest_framework import status

from api.serializers import ArticleSerializer
from api.utils import get_articles_from_file, get_article_data


class ArticleAPIView(AsyncAPIView):
    async def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        articles_info = []

        if article := serializer.validated_data.get('article'):
            article_info = await get_article_data(article)
            articles_info.append(article_info)
        elif file := serializer.validated_data.get('file'):
            for article in get_articles_from_file(file):
                article_info = await get_article_data(article)
                articles_info.append(article_info)
        
        return JsonResponse([item.dict() for item in articles_info], status=status.HTTP_200_OK, safe=False)