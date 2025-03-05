from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
  path("profile/", views.profile, name = "profile"),
  path("login/", views.log_in, name = "login"), # connexion
  path("register/", views.register, name = "register"), # inscription

  path('deconnexion/', views.deconnexion, name='logout'), # deconnexion
]
