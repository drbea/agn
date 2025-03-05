from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.urls import reverse

User = get_user_model()

# Create your views here.

def index(request):

	return render(request, "home/index.html", context={})


def about(request):

	return render(request, "home/about.html", context={})


def profile(request):

	return render(request, "home/profile.html", context={})


def deconnexion(request):
    logout(request)
    return redirect('home:index')


def log_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'redirect_url': reverse("home:index")}) # Réponse JSON en cas de succès avec redirection
        else:
            return JsonResponse({'success': False, 'error': "Nom d'utilisateur ou mot de passe incorrect."}) # Réponse JSON en cas d'erreur
    return render(request, "home/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return JsonResponse({'success': True, 'redirect_url': reverse("home:index")}) # Redirection en cas de succès
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}) # Erreur si l'inscription échoue
    return render(request, "home/sign_in.html")

