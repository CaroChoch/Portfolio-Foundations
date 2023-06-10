from django.contrib import admin
from .models import Category


# Enregistrement du modèle Category sur le site d'administration.
admin.site.register(Category)