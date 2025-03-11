from django.shortcuts import render
from . models import Article, Category, Topic
# Create your views here.

def index(request):

    return render(request, "blog/base_blog.html")


def article_detail(request, article_id):
    object = get_object_or_404(Article, pk = article_id)

    context = {
        "article": object,
    }
    return render(request, "blog/article_detail.html", context)

def created_article(request):

    context = {
        # "article": object,
    }
    return render(request, "blog/created_article.html", context)
