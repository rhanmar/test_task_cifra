from django.db import models
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    """Information about Article."""

    name = models.CharField(
        verbose_name=_("Article Name"),
        max_length=80,
    )

    short_description = models.CharField(
        verbose_name=_("Article Short Description"),
        max_length=80,
    )

    long_description = models.CharField(
        verbose_name=_("Article Long Description"),
        max_length=254,
    )

    type = models.ForeignKey(
        "news.ArticleType",
        verbose_name=_("Article Type"),
        related_name='articles',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """Return Article name."""
        return self.name


class ArticleType(models.Model):
    """Information about Article Type."""

    name = models.CharField(
        verbose_name=_("Article Type Name"),
        max_length=80,
    )

    color = models.CharField(
        verbose_name=_("Article Type Color"),
        max_length=80,
    )

    def __str__(self):
        """Return Article Type name."""
        return f"{self.name}, {self.color}"
