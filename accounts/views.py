from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.urls import reverse

User = get_user_model()

# Create your views here.
def deconnexion(request):
    logout(request)
    return redirect('home:index')


def profile(request):

	return render(request, "home/profile.html", context={})


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
    return render(request, "accounts/login.html")

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.create_user(username=username, password=password, email = email)
            user.first_name = first_name
            user.last_name = last_name
            login(request, user)
            return JsonResponse({'success': True, 'redirect_url': reverse("home:index")}) # Redirection en cas de succès
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}) # Erreur si l'inscription échoue
    return render(request, "accounts/register.html")
