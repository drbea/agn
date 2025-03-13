from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    # path("detail/<int:article_id>", views.article_detail, name="article_detail")
    path("add-article/", views.created_article, name="created_article"),
    path("article_detail/<int:article_id>/", views.article_detail, name="article_detail"),
]
