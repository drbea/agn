from django.contrib import admin
from .models import Testimonial, Image, Partenaire

# Register your models here.

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'approved')  # Colonnes à afficher dans la liste
    list_filter = ('approved',)  # Permet de filtrer par témoignages approuvés
    search_fields = ('name', 'message')  # Recherche par nom ou message
    actions = ['approve_testimonials']  # Ajouter une action personnalisée

    # Action pour approuver les témoignages
    def approve_testimonials(self, request, queryset):
        queryset.update(approved=True)
    approve_testimonials.short_description = 'Approuver les témoignages sélectionnés'


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Partenaire)
class PartenaireAdmin(admin.ModelAdmin):
    pass