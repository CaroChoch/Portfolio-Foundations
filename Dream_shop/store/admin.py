from django.contrib import admin
from .models import Product, Variation


class ProductAdmin(admin.ModelAdmin):
    """
    Configuration de l'administration pour le modèle Product.
    """
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    # Spécifie les champs à afficher dans la vue liste du panneau d'administration
    prepopulated_fields = {'slug': ('product_name',)}
    # Spécifie les champs à pré-remplir en se basant sur d'autres champs

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')

# Enregistre le modèle Product avec sa configuration d'administration correspondante
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
