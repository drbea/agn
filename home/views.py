from django.shortcuts import render
from products.models import Product
# Create your views here.
def index(request):
    products = Product.objects.all()[0:3:-1]
    context = {
        'products': products
    }

    return render(request, "home/index.html", context)

def contact(request):
    return render(request, 'home/Contact.html')

def apropos(request):
    return render(request, 'home/Apropos.html')

def livraison(request):
<<<<<<< HEAD
    return render(request, 'home/Livraison.html')

def offres(request):
    return render(request, 'home/Offres.html')
=======
    return render(request, 'home/livraison.html')
>>>>>>> bb002949fb2d15105139e837075de82624afaf5f
