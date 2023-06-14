from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category


def store(request, category_slug=None):
    """
    Vue pour afficher la page principale du magasin.
  
    Si un slug de catégorie est fourni, cette vue filtrera les produits 
    en fonction de cette catégorie. Sinon, tous les produits disponibles 
    seront affichés.

    Arguments:
    request -- Requête HTTP
    category_slug -- Slug de la catégorie (par défaut: None)

    Retourne:
    Réponse HTTP avec le rendu de la page du magasin
    """
  
    categories = None
    products = None

    # Si un slug de catégorie est fourni
    if category_slug is not None:
        # Récupérer la catégorie correspondante ou lever une erreur 404 si elle n'existe pas
        categories = get_object_or_404(Category, slug=category_slug)
        
        # Filtrer les produits disponibles en fonction de cette catégorie
        products = Product.objects.filter(category=categories, is_available=True)
        
        # Compter le nombre de produits disponibles dans cette catégorie
        product_count = products.count()
    else:
        # Si aucun slug de catégorie n'est fourni, récupérer tous les produits disponibles
        products = Product.objects.all().filter(is_available=True)
        
        # Compter le nombre total de produits disponibles
        product_count = products.count()

    # Créer le contexte avec les produits et le nombre de produits
    context = {
        'products': products,
        'product_count': product_count,
    }

    # Rendre la page du magasin avec le contexte créé
    return render(request, 'store/store.html', context)
