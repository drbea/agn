from django.shortcuts import render

# Create your views here.
def index(request):

    context = {}
    return render(request, "home/index.html", context)

def contact(request):
    return render(request, 'home/Contact.html')

def apropos(request):
    return render(request, 'home/Apropos.html')