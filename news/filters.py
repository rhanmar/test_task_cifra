from django_filters import rest_framework as filters

from news.models import Article


class ArticlesFilter(filters.FilterSet):
    """Filter for Articles by type name and type color."""

    type_name = filters.CharFilter(field_name="type__name")
    type_color = filters.CharFilter(field_name="type__color")

    class Meta:
        model = Article
        fields = ["type"]
