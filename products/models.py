from django.db import models
from django.contrib.auth import get_user_model

from django.utils.timezone import now

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    # def count_reactions(self):
    #     """Retourne un dictionnaire avec le nombre total de chaque type de réaction."""
    #     return self.reactions.values('type_reaction').annotate(count=models.Count('type_reaction'))


# class Commentaire(models.Model):
#     autheur = models.ForeignKey(User, on_delete = models.CASCADE)
#     publication = models.ForeignKey(Publication, on_delete = models.CASCADE)
#     date_creation = models.DateTimeField(auto_now_add = True)
#     date_mis_a_jour = models.DateTimeField(auto_now = True)
#     contenu = models.TextField(default = "commentaire ici")

#     class Meta:
#         ordering = ['-date_mis_a_jour', '-date_creation']

#     def __str__(self):
#         return self.contenu[:50]


# class Reaction(models.Model):
#     autheur = models.ForeignKey(User, on_delete=models.CASCADE)
#     produit = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='reactions')
#     type_reaction = models.CharField(
#         max_length=50,
#         choices=[
#             ("like", "like"),
#             ("dislike", "dislike"),
#         ]
#     )
#     date_reaction = models.DateTimeField(auto_now=True)

#     class Meta:
#         unique_together = ('autheur', 'produit', 'type_reaction')  # Empêche plusieurs réactions du même type par utilisateur/publication

#     def __str__(self):
#         return f"{self.autheur} a réagi sur {self.produit} avec {self.type_reaction}"



