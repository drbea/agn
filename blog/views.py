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
    categories = Category.objects.all()
    topics = Topic.objects.all()
    
    if request.method == "POST":
        title = request.POST.get("title")
        introduction = request.POST.get("introduction")
        categories_selected = request.POST.getlist("categories")
        topics_selected = request.POST.getlist("topics")
        
        subtitle_1 = request.POST.get("subtitle_1")
        contenu_1 = request.POST.get("contenu_1")
        subtitle_2 = request.POST.get("subtitle_2")
        contenu_2 = request.POST.get("contenu_2")
        subtitle_3 = request.POST.get("subtitle_3")
        contenu_3 = request.POST.get("contenu_3")
        subtitle_4 = request.POST.get("subtitle_4")
        contenu_4 = request.POST.get("contenu_4")
        
        image = request.FILES.get("image")
        image_1 = request.FILES.get("image_1")
        image_2 = request.FILES.get("image_2")
        image_3 = request.FILES.get("image_3")
        image_4 = request.FILES.get("image_4")
        
        article = Article.objects.create(
            title=title,
            introduction=introduction,
            author=request.user,
            image=image,
            subtitle_1=subtitle_1,
            contenu_1=contenu_1,
            image_1=image_1,
            subtitle_2=subtitle_2,
            contenu_2=contenu_2,
            image_2=image_2,
            subtitle_3=subtitle_3,
            contenu_3=contenu_3,
            image_3=image_3,
            subtitle_4=subtitle_4,
            contenu_4=contenu_4,
            image_4=image_4
        )
        
        article.categories.set(categories_selected)
        article.topics.set(topics_selected)
        
        return redirect("blog:index")  # Redirection après la création de l'article
    
    return render(request, "blog/create_article.html", {"categories": categories, "topics": topics})
