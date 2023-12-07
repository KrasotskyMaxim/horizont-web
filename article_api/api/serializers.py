from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.constants import XLSX_CONTENT_TYPE


class ArticleSerializer(serializers.Serializer):
    article = serializers.IntegerField(required=False)
    file = serializers.FileField(required=False)

    def validate(self, data):
        article = data.get('article')
        file = data.get('file')

        if not article and not file:
            raise ValidationError("Either 'article' or 'file' must be provided.")

        if article and file:
            raise ValidationError("Provide either 'article' or 'file', not both.")

        if file:
            if file.content_type != XLSX_CONTENT_TYPE:
                raise ValidationError("Invalid file format. Only xlsx files are supported.")

        return data
    