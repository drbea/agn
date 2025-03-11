from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
  path("", views.index, name = "index"),
  path('contact/', views.contact, name='contact'),
  path('apropos/', views.apropos, name='apropos'),
  path('livraison/', views.livraison, name='livraison'),
  path('offres/', views.offres, name='offres'),  # Add this line
]
