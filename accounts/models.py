from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile_pic = models.ImageField(upload_to = "profile_pic", default = "img/profile_pic")
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    preferences = models.JSONField(default=dict, blank=True, null=True)
    # wishlist = models.ManyToManyField('Product', related_name='wishlisted_by', blank=True)
    loyalty_points = models.IntegerField(default=0)
    city = models.CharField(max_length=20, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username



#
# class Order(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     product = models.ForeignKey('Product', on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     order_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.product.name} ordered by {self.user.username}'
