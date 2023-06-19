from django.contrib import admin
from .models import Cart, CartItem


# Enregistrement des modèles Cart et CartItem dans l'interface d'administration
admin.site.register(Cart)
admin.site.register(CartItem)
