from django.contrib import admin
from . models import Category, Product, PaymentMethod
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'image', 'category']

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    pass
    
    # list_display = ['name', 'description']
