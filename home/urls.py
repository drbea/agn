from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
  path("", views.index, name="index"),
  path('contact/', views.contact, name='contact'),
  path('contact/success/', views.contact_success, name='contact_success'),
  path('apropos/', views.apropos, name='apropos'),
  path('livraison/', views.livraison, name='livraison'),
  path('livraison/success/', views.livraison_success, name='livraison_success'),
  path('offres/', views.offres, name='offres'),
  path('offres/<int:offer_id>/', views.offer_detail, name='offer_detail'),
]
