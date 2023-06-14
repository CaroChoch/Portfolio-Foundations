from django.shortcuts import render
from store.models import Product, Category


def home(request):
    """
    Vue pour afficher la page d'accueil du site.
    """

    # Récupérer tous les produits disponibles
    category = Category.objects.get(category_name="Best seller")
    products = Product.objects.filter(is_available=True, category=category)[:3]

    # Préparer le contexte avec les produits pour l'affichage dans le template
    context = {
        'products': products,
    }

    # Renvoyer la réponse avec le template 'home.html' et le contexte
    return render(request, 'home.html', context)
