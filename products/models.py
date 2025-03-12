from django.db import models
from django.contrib.auth import get_user_model

from django.utils.timezone import now

User = get_user_model()

class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)
    # Ajoutez d'autres champs si nécessaire (par exemple, une image, une description, etc.)

    def __str__(self):
        return self.name

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



class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Un utilisateur a un seul panier
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Panier de {self.user.username}"

    def get_total(self):
        return sum(item.get_subtotal() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} dans le panier de {self.cart.user.username}"

    def get_subtotal(self):
        return self.product.price * self.quantity


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




### AJOUTER PLUSIEUR images
# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     images = models.ManyToManyField(Image)  # Lien avec la table Image
#
# class Image(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='product_images/')



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande #{self.id} par {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} dans la commande #{self.order.id}"
