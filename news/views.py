from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets

from news import serializers
from news.filters import ArticlesFilter
from news.models import Article, ArticleType


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to create, show, update and delete Article.
    """
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']


class ArticleTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to create, show, update and delete ArticleType.
    """
    queryset = ArticleType.objects.all()
    serializer_class = serializers.ArticleTypeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'color']


class ArticleExtendedListViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    API endpoint that allows to show Articles extended list with ArticleType info.
    """

    queryset = Article.objects.all()
    serializer_class = serializers.ArticleExtendedListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArticlesFilter
