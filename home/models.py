from django.db import models
from django.urls import reverse

from products.models import Product

# Create your models here.

class Image(models.Model):
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)


class Testimonial(models.Model):
    name = models.CharField(max_length=255)  # Le nom de la personne qui laisse le témoignage
    message = models.TextField()  # Le contenu du témoignage
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création du témoignage
    approved = models.BooleanField(default=False)  # Champ pour savoir si le témoignage est approuvé ou non
    email = models.EmailField()  # Optionnel : l'email de la personne
    # image = models.ImageField(upload_to='testimonials/', null=True, blank=True)  # Optionnel : une image du témoignage (facultatif)
    images = models.ManyToManyField(Image)  # Lien avec la table Image

    def __str__(self):
        return f"Témoignage de {self.name}"

    class Meta:
        verbose_name = 'Témoignage'
        verbose_name_plural = 'Témoignages'

class Partenaire(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='partenaires/', null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Partenaire'
        verbose_name_plural = 'Partenaires'

class SpecialOffer(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='offers/')
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home:offer_detail', args=[str(self.id)])
