from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from carts.views import _cart_id
from carts.models import CartItem
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse


def store(request, category_slug=None):
    """
    Vue pour afficher la page principale du magasin.

    Arguments:
    request -- Requête HTTP
    category_slug -- Slug de la catégorie (par défaut: None)

    Retourne:
    Réponse HTTP avec le rendu de la page du magasin
    """
    # Initialiser les variables
    categories = None
    products = None
    page_title = "Collection Complète"

    # Si un slug de catégorie est fourni
    if category_slug is not None:
        # Récupérer la catégorie correspondante ou lever une erreur 404 si elle n'existe pas
        categories = get_object_or_404(Category, slug=category_slug)
        
        # Filtrer les produits disponibles en fonction de cette catégorie
        products = Product.objects.filter(category=categories, is_available=True)

        # Paginator pour la page store avec 9 elements par page
        paginator = Paginator(products, 9)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        
        # Compter le nombre de produits disponibles dans cette catégorie
        product_count = products.count()
        page_title = categories.category_name
    else:
        # Si aucun slug de catégorie n'est fourni, récupérer tous les produits disponibles
        products = Product.objects.filter(is_available=True).order_by('id')

        # Filtrer les produits par genre (homme ou femme) et par type de produit
        gender = request.GET.get('gender')
        category = request.GET.get('category')
        if gender == 'men':
            products = products.filter(category__gender='H')
            page_title = "Collection Homme"
        elif gender == 'women':
            products = products.filter(category__gender='F')
            page_title = "Collection Femme"
        
        if category == 'clothingMen':
            products = products.filter(category__product_type='A')
            page_title = "Vêtements Homme"
        elif category == 'clothingWomen':
            products = products.filter(category__product_type='B')
            page_title = "Vêtements Femme"
        elif category == 'clothingAccessMen':
            products = products.filter(category__product_type='Y')
            page_title = "Accessoires Homme"
        elif category == 'clothingAccessWomen':
            products = products.filter(category__product_type='X')
            page_title = "Accessoires Femme"

        # Pagination de store avec 9 elements par page
        paginator = Paginator(products, 9)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)

        # Compter le nombre total de produits disponibles
        product_count = products.count()

    # Créer le contexte avec les produits, le nombre de produits et le titre de la page
    context = {
        'products': paged_products,
        'product_count': product_count,
        'page_title': page_title,
    }

    # Rendre la page du magasin avec le contexte créé
    return render(request, 'store/store.html', context)



def product_detail(request, category_slug, product_slug):
    """
    Vue pour afficher le détail d'un produit spécifique.
    """
    try:
        # Récupérer le produit spécifique ou lever une exception si il n'existe pas
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e

    # Créer le contexte avec le produit et les liens des catégories
    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }

    # Rendre la page de détail du produit avec le contexte créé
    return render(request, 'store/product_detail.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)