from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    """
    Configuration de l'administration pour le modèle Product.
    """
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    # Spécifie les champs à afficher dans la vue liste du panneau d'administration

    prepopulated_fields = {'slug': ('product_name',)}
    # Spécifie les champs à pré-remplir en se basant sur d'autres champs

admin.site.register(Product, ProductAdmin)
# Enregistre le modèle Product avec sa configuration d'administration correspondante
