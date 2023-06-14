from django.shortcuts import render
from store.models import Product, Sub_Category

def home(request):
    """
    Vue pour afficher la page d'accueil du site.
    """
    try:
        # Récupérer la sous-catégorie 'Best Seller'
        best_seller = Sub_Category.objects.get(name="Best Seller")
    except Sub_Category.DoesNotExist:
        best_seller = None  # Gérer le cas où la sous-catégorie 'Best Seller' n'existe pas

    # Récupérer tous les produits disponibles qui sont dans la sous-catégorie 'Best Seller'
    products = Product.objects.filter(is_available=True, category=best_seller)[:3]

    # Préparer le contexte avec les produits pour l'affichage dans le template
    context = {
        'products': products,
    }

    # Renvoyer la réponse avec le template 'home.html' et le contexte
    return render(request, 'home.html', context)
