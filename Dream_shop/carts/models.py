from django.db import models
from store.models import Product, Variation


class Cart(models.Model):
  """
  Modèle représentant un panier d'achat.

  Champs :
      - cart_id (CharField) : Identifiant unique du panier.
      - date_added (DateField) : Date à laquelle le panier a été créé.

  Méthodes :
      - __str__ : Renvoie une représentation textuelle du panier.
  """
  cart_id = models.CharField(max_length=250, blank=True)
  date_added = models.DateField(auto_now_add=True)

  def __str__(self):
    """
    Renvoie une représentation textuelle du panier.
    """
    return self.cart_id


class CartItem(models.Model):
  """
  Modèle représentant un article dans un panier d'achat.

  Champs :
      - product (ForeignKey vers Product) : Le produit associé à l'article.
      - cart (ForeignKey vers Cart) : Le panier auquel l'article appartient.
      - quantity (IntegerField) : La quantité de l'article dans le panier.
      - is_active (BooleanField) : Indique si l'article est actif dans le panier.

  Méthodes :
      - __str__ : Renvoie une représentation textuelle de l'article.
    """
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  variations = models.ManyToManyField(Variation, blank=True)
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  is_active = models.BooleanField(default=True)

  def sub_total(self):
    return self.product.price * self.quantity

  def __str__(self):
    """
    Renvoie une représentation textuelle de l'article.
    """
    return str(self.product)