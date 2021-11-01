from rest_framework import routers

from news import views

router = routers.DefaultRouter()

router.register("articles", views.ArticleViewSet, basename="articles")
router.register("articles-ext", views.ArticleExtendedListViewSet, basename="articles-ext")
router.register("article-types", views.ArticleTypeViewSet, basename="articles-types")

urlpatterns = router.urls
