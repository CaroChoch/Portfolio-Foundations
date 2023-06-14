from django.contrib import admin
from .models import Category, Sub_Category


class CategoryAdmin(admin.ModelAdmin):
  """
  Configuration de l'administration pour le modèle Category.
  """
  prepopulated_fields = {'slug': ('category_name',)}
  list_display = ('category_name', 'slug', 'gender',)

# Enregistrement du modèle Category sur le site d'administration.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Sub_Category)

