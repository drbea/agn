from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from products.models import Product
from .models import Partenaire, SpecialOffer

# Create your views here.
def index(request):
    products = Product.objects.all()[0:3:-1]
    context = {
        'products': products,
        'partenaires': Partenaire.objects.all(),
    }

    return render(request, "home/index.html", context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        preferred_contact = request.POST.get('preferred_contact')

        # Send email to the administrator
        send_mail(
            f'Contact Form Submission: {subject}',
            f'Nom: {name}\nEmail: {email}\nTéléphone: {phone}\nPréférence de contact: {preferred_contact}\n\nMessage:\n{message}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )

        return redirect('home:contact_success')

    return render(request, 'home/Contact.html')

def contact_success(request):
    return render(request, 'home/Contact_success.html')

def apropos(request):
    return render(request, 'home/Apropos.html')

def livraison(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        message = request.POST.get('message')

        # Send email to the administrator
        send_mail(
            'Nouvelle demande de livraison',
            f'Nom: {name}\nTéléphone: {phone}\nAdresse: {address}\nMessage: {message}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )

        return redirect('home:livraison_success')

    return render(request, 'home/Livraison.html')

def livraison_success(request):
    return render(request, 'home/Livraison_success.html')

def offres(request):
    special_offers = SpecialOffer.objects.all()
    context = {
        'special_offers': special_offers
    }
    return render(request, 'home/Offres.html', context)

def offer_detail(request, offer_id):
    offer = get_object_or_404(SpecialOffer, id=offer_id)
    context = {
        'offer': offer
    }
    return render(request, 'home/offer_detail.html', context)
