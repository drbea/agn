
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
# from django.contrib import messages
from . models import Category, Product

# Create your views here.

def index(request):

    context =  {
        # 'categories': categories,
        }

    return render(request, 'boutique/index.html', context)

def product_category(request, category_id):
    query_search = request.GET.get('query_search')
    categories = Category.objects.all()
    selected_category = None

    products = Product.objects.all()

    if category_id:
        selected_category = get_object_or_404(Category, id = category_id)
        products = Product.objects.filter(category = selected_category)

    page = request.GET.get('page')
    paginator = Paginator(products, 3)
    page_objects = paginator.get_page(page)

    context =  {
        'categories': categories,
        'products': products,
        'page_objects': page_objects,
        'query_search': query_search,
        'selected_category': selected_category,
        }

    return render(request, 'boutique/produits.html', context)



def detail_product(request, product_id):
    product = Product.objects.get(id = product_id)
    context = {
        "product": product,
    }
    return render(request, "boutique/detail_product.html", context)


def create_product(request):
    categories = Category.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        image = request.POST.get("image")
        category_name = request.POST.get("category")

        if any(category.name == category_name for category in categories):
            # messages.error(request, "A category with that name already exists.")
            category_name = category_name
        else:
            new_category = Category.objects.create(name=category_name)
            new_product = Product.objects.create(
                name=name, description=description, price=price, image=image, category=new_category
            )
            new_product.save()
            return redirect("boutique:index")

    context = {"categories": categories}
    return render(request, "boutique/create_product.html", context)





def product_list(request):
    query_search = request.GET.get('query_search')
    categories = Category.objects.all()
    products = Product.objects.all()
    if query_search:
        products = Product.objects.filter(Q(name__icontains=query_search) |
                                          Q(description__icontains=query_search) |
                                          Q(category__name__icontains=query_search)
                                          )

    page = request.GET.get('page')
    paginator = Paginator(products, 3)
    page_objects = paginator.get_page(page)

    context =  {
        'categories': categories,
        'products': products,
        'page_objects': page_objects,
        'query_search': query_search
        }
    return render(request, 'products/list_product.html', context)



def panier(request):
    context = {
            # "product": product,
        }
    return render(request, "boutique/panier.html", context)
