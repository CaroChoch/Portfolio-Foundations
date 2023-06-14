from django.shortcuts import render
from store.models import Product, Category


def home(request):
    """
    Vue pour afficher la page d'accueil du site.
    """

    # Récupérer tous les produits disponibles
    category = Category.objects.get(category_online="Best seller")
    products = Product.objects.filter(is_available=True, category=category)[:3]

    women_links = Category.objects.filter(product_type='B')
    men_links = Category.objects.filter(product_type='A')
    
    women_acc = Category.objects.filter(product_type='X')
    men_acc = Category.objects.filter(product_type='Y')


    # Préparer le contexte avec les produits pour l'affichage dans le template
    context = {
        'products': products,
        'women_links': women_links,
        'women_acc': women_acc,
        'men_links': men_links,
        'men_acc': men_acc,
    }

    # Renvoyer la réponse avec le template 'home.html' et le contexte
    return render(request, 'home.html', context)
