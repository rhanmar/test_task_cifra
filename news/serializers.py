from rest_framework import serializers

from news.models import Article, ArticleType


class ArticleSerializer(serializers.ModelSerializer):
    """Serializer for Article model."""

    class Meta:
        model = Article
        fields = (
            "id",
            "name",
            "short_description",
            "long_description",
            "type"
        )


class ArticleExtendedListSerializer(serializers.ModelSerializer):
    """Serializer for Article extended list."""

    type_name = serializers.CharField(source="type.name")
    type_color = serializers.CharField(source="type.color")

    class Meta:
        model = Article
        fields = (
            "name",
            "short_description",
            "long_description",
            "type_name",
            "type_color"
        )


class ArticleTypeSerializer(serializers.ModelSerializer):
    """Serializer for Article Type model."""

    class Meta:
        model = ArticleType
        fields = ("id", "name", "color")
