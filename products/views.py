from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
# from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import Product, Cart, CartItem, Order, OrderItem
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

from . models import Category, Product, PaymentMethod
# from .models import

# Create your views here.

def index(request):
    context =  {
        # 'categories': categories,
        }
    return render(request, 'boutique/index.html', context)


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


def filter_by_category(request, category_id):
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

    return render(request, 'products/list_product.html', context)



def product_detail(request, product_id):
    product = Product.objects.get(id = product_id)
    context = {
        "product": product,
        "recents_products": Product.objects.all()[:5]
    }
    return render(request, "products/product_detail.html", context)


def add_product(request):
    categories = Category.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        image = request.POST.get("image")
        category_name = request.POST.get("category_name")

        if any(category.name == category_name for category in categories):
            # messages.error(request, "A category with that name already exists.")
            category_name = category_name
        else:
            new_category = Category.objects.create(name=category_name)
            new_product = Product.objects.create(
                name=name, description=description, price=price, image=image, category=new_category
            )
            new_product.save()
            return redirect("product:product_list")

    context = {"categories": categories}
    return render(request, "products/add_product.html", context)




@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('products:panier')  # Rediriger vers la vue du panier


@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()
    total = cart.get_total()
    context = {'cart_items': cart_items, 'total': total}
    return render(request, 'products/panier.html', context)


@login_required
@require_POST
def update_cart(request):
    try:
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity'))
        item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        item.quantity = quantity
        item.save()
        cart = item.cart
        return JsonResponse({
            'quantity': item.quantity,
            'subtotal': str(item.get_subtotal()),
            'cart_total': str(cart.get_total())
        })
    except Exception as e:
        print(f"Error in update_cart: {e}") # Ajout d'un print
        return JsonResponse({'error': str(e)}, status=500)

@login_required
@require_POST
def remove_item_ajax(request):
    try:
        item_id = request.POST.get('item_id')
        item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        cart = item.cart
        item.delete()
        return JsonResponse({'cart_total': str(cart.get_total())})
    except Exception as e:
        print(f"Error in remove_item_ajax: {e}") # Ajout d'un print
        return JsonResponse({'error': str(e)}, status=500)


@login_required
def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()
    total = cart.get_total()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Récupération des données du formulaire
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']

            # Création de la commande
            order = Order.objects.create(
                user=request.user,
                first_name=first_name,
                last_name=last_name,
                email=email,
                address=address,
                city=city,
                total=total
            )

            # Création des éléments de commande
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )

            # Vider le panier
            cart.items.all().delete()

            # Redirection vers la confirmation de commande
            return redirect('products:payment_selection')
    else:
        form = OrderForm()

    context = {'cart_items': cart_items, 'total': total, 'form': form}
    return render(request, 'products/checkout.html', context)



def payment_selection(request):
    payment_methods = PaymentMethod.objects.all()  # Récupérer tous les modes de paiement
    if request.method == "POST":
        return redirect("products:process_payment")
        
    context = {'payment_methods': payment_methods}
    return render(request, 'products/payment_selection.html', context)


def process_payment(request):
    if request.method == 'POST':
        payment_method_id = request.POST.get('payment_method')
        payment_method = PaymentMethod.objects.get(id=payment_method_id)
        # Traitez le paiement en utilisant le mode de paiement sélectionné
        # ...
        return redirect('products:payment_confirmation')  # Redirigez vers la confirmation de paiement
    else:
        return redirect('products:payment_selection')


@login_required
def order_confirmation(request):
    return render(request, 'products/order_confirmation.html')
# <<<<<<< HEAD

def product_search(request):
    query = request.GET.get('query')
    products = Product.objects.filter(name__icontains=query)
    context = {
        'products': products,
        'query': query
    }
    return render(request, 'products/product_search.html', context)



# =======
# >>>>>>> bdc99dec56d14fd7a6d84b3f405c2791786073a1
