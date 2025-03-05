from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
  path("", views.index, name = "index"),
  path("about/", views.about, name = "about"),
  path("profile/", views.profile, name = "profile"),

  path("login/", views.log_in, name = "login"),
  path("register/", views.register, name = "register"),
  
  path('deconnexion/', views.deconnexion, name='logout'),
]
