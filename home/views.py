from django.shortcuts import render
from products.models import Product
from .models import Partenaire #, Testimonial, Image
# Create your views here.
def index(request):
    products = Product.objects.all()[0:3:-1]
    context = {
        'products': products,
        'partenaires': Partenaire.objects.all(),
    }

    return render(request, "home/index.html", context)

def contact(request):
    return render(request, 'home/Contact.html')

def apropos(request):
    return render(request, 'home/Apropos.html')

def livraison(request):
    return render(request, 'home/Livraison.html')

def offres(request):
    return render(request, 'home/Offres.html')
