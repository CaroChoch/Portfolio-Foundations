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

    women_links = Category.objects.filter(product_type='B')
    men_links = Category.objects.filter(product_type='A')
    women_acc = Category.objects.filter(product_type='X')
    men_acc = Category.objects.filter(product_type='Y')
    men_links_all = Category.objects.filter(gender='H')
    women_links_all = Category.objects.filter(gender='F')

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
        products = Product.objects.filter(is_available=True)

        # Filtrer les produits par genre (homme ou femme)
        gender = request.GET.get('gender')
        if gender == 'men':
            products = products.filter(category__gender='H')
        elif gender == 'women':
            products = products.filter(category__gender='F')
        
        # Compter le nombre total de produits disponibles
        product_count = products.count()

    # Créer le contexte avec les produits et le nombre de produits
    context = {
        'products': products,
        'product_count': product_count,
        'women_links': women_links,
        'women_acc': women_acc,
        'men_links': men_links,
        'men_acc': men_acc,
    }

    # Rendre la page du magasin avec le contexte créé
    return render(request, 'store/store.html', context)
