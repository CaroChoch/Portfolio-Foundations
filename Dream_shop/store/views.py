from django.shortcuts import render
from .models import Product


def store(request):
  """
  Vue pour afficher la page principale du magasin.
  """
  products = Product.objects.all().filter(is_available=True) # Récupère tous les produits disponibles

  product_count = products.count() # Compte le nombre de produits disponibles

  # Créer le contexte avec les produits et le nombre de produits
  context = {
    'products': products,
    'product_count': product_count,
  }
  return render(request, 'store/store.html', context)
