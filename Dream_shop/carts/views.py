from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product, Variation
from category.models import Category
from .models import Cart, CartItem
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


def _cart_id(request):
  """
    Obtient l'ID du panier de la session en cours.

    Args:
        request: L'objet de requête Django.

    Returns:
        str: L'ID du panier de la session.

  """
  cart = request.session.session_key
  if not cart:
    cart = request.session.create()
  return cart


def add_cart(request, product_id):
  """
    Ajoute un produit au panier.

    Args:
        request: L'objet de requête Django.
        product_id (int): L'ID du produit à ajouter.

    Returns:
        django.shortcuts.redirect: Redirection vers la page du panier.

  """
  # Obtient le produit à partir de l'ID
  product = Product.objects.get(id=product_id)
  # Liste des variations sélectionnées par l'utilisateur
  product_variation = []
  
  if request.method == 'POST':
    for item in request.POST:
      key = item
      value = request.POST[key]
      try:
        # Vérifie si la variation existe pour le produit
        variation = Variation.objects.get(product=product, variation_category__iexact=key, variation_value__iexact=value)
         # Ajoute la variation à la liste des variations du produit
        product_variation.append(variation)
      except:
        pass

  try:
    # Obtient le panier existant à partir de l'ID de session
    cart = Cart.objects.get(cart_id=_cart_id(request))
  except Cart.DoesNotExist:
    # Crée un nouveau panier s'il n'existe pas
    cart = Cart.objects.create(cart_id = _cart_id(request))

  cart.save()

  # Vérifie si le produit avec les mêmes variations existe déjà dans le panier
  cart_items = CartItem.objects.filter(product=product, cart=cart)
  added = False

  for cart_item in cart_items:
    existing_variations = cart_item.variations.all()
    if set(existing_variations) == set(product_variation):
      # Augmente la quantité de l'article dans le panier
      cart_item.quantity += 1
      cart_item.save()
      added = True
      break

  if not added:
    # Crée un nouvel article de panier avec la quantité 1
    cart_item = CartItem.objects.create(
      product=product,
      quantity=1,
      cart=cart,
    )
    if len(product_variation) > 0:
      # Ajoute les variations sélectionnées à l'article de panier
      cart_item.variations.clear()
      cart_item.variations.add(*product_variation)
    cart_item.save()

  return redirect('cart')


def remove_cart(request, product_id, cart_item_id):
  """
    Supprime un produit du panier ou réduit sa quantité.

    Args:
        request: L'objet de requête Django.
        product_id (int): L'ID du produit à supprimer du panier.
        cart_item_id (int): L'ID de l'élément du panier à supprimer ou réduire.

    Returns:
        django.shortcuts.redirect: Redirection vers la page du panier.

  """
  # Obtient le panier à partir de l'ID de session
  cart = Cart.objects.get(cart_id=_cart_id(request))
  # Obtient le produit à partir de l'ID
  product = get_object_or_404(Product, id=product_id)
  try:
    # Obtient l'élément du panier correspondant au produit et à l'ID de l'élément
    cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
    if cart_item.quantity > 1:
      # Réduit la quantité de l'élément du panier
      cart_item.quantity -= 1
      cart_item.save()
    else:
      # Supprime complètement l'élément du panier
      cart_item.delete()
  except:
    pass
  return redirect('cart')


def remove_cart_item(request, product_id, cart_item_id):
  """
    Supprime complètement un produit du panier.

    Args:
        request: L'objet de requête Django.
        product_id (int): L'ID du produit à supprimer du panier.
        cart_item_id (int): L'ID de l'élément du panier à supprimer.

    Returns:
        django.shortcuts.redirect: Redirection vers la page du panier.

  """
  # Obtient le panier à partir de l'ID de session
  cart = Cart.objects.get(cart_id=_cart_id(request))
  # Obtient le produit à partir de l'ID
  product = get_object_or_404(Product, id=product_id)
  # Obtient l'élément du panier correspondant au produit et à l'ID de l'élément
  cart_item = CartItem.objects.get(product=product, cart=cart.id, id=cart_item_id)
  # Supprime complètement l'élément du panier
  cart_item.delete()
  return redirect('cart')


def cart(request, total=0, quantity=0, cart_items=None):
  """
    Affiche le panier d'achat.

    Args:
        request: L'objet de requête Django.
        total (float): Le total du panier (par défaut : 0).
        quantity (int): La quantité totale des produits dans le panier (par défaut : 0).
        cart_items (QuerySet): Les éléments du panier (par défaut : None).

    Returns:
        django.shortcuts.render: Rendu de la page du panier.

  """
  tax = 0
  grand_total = 0
  try:
    # Obtient le panier à partir de l'ID de session
    cart = Cart.objects.get(cart_id=_cart_id(request))
    # Obtient tous les éléments du panier actifs
    cart_items = CartItem.objects.filter(cart=cart, is_active=True)
    for cart_item in cart_items:
      # Calcule le total en multipliant le prix du produit par sa quantité dans le panier
      total += (cart_item.product.price * cart_item.quantity)
      # Calcule la quantité totale de produits dans le panier
      quantity += cart_item.quantity
    # Calcule la taxe en appliquant un pourcentage fixe (20%) sur le total
    tax = (20 * total)/100
  except ObjectDoesNotExist:
    pass

  context = {
    'total': total,
    'quantity': quantity,
    'cart_items': cart_items,
    'tax': tax,
  }
  return render(request, 'store/cart.html', context)
