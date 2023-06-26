from django.test import TestCase
from django.contrib.auth.models import User
from carts.models import Cart, CartItem
from store.models import Product
from category.models import Category
from datetime import date
from django.utils import timezone


class CartModelTest(TestCase):
  """
  Classe de test pour le modèle Cart.
  """
  @classmethod
  def setUpTestData(cls):
    """
    Configuration des données de test qui ne changent pas
    """
    test_category = Category.objects.create(category_name='test category', slug='test-category')
    Product.objects.create(product_name='Test product', price=10, category=test_category)

  def setUp(self):
    """
    Configuration des données de test spécifiques à chaque méthode de test
    """
    self.cart = Cart.objects.create(cart_id='1234')
    self.product = Product.objects.get(id=1)
    self.cart_item = CartItem.objects.create(product=self.product, cart=self.cart, quantity=1)

  def test_cart_creation(self):
    """
    Vérifie si le panier a été créé avec succès
    """
    self.assertTrue(isinstance(self.cart, Cart))
  
  def test_cart_str(self):
    """
    Vérifie si la méthode __str__ du modèle Cart renvoie l'identifiant du panier.
    """
    self.assertEqual(str(self.cart), self.cart.cart_id)
  
  def test_cart_item_creation(self):
    """
    Vérifie si nous pouvons créer un article de panier avec succès.
    """
    self.assertTrue(isinstance(self.cart_item, CartItem))

  def test_cart_item_str(self):
    """
    Vérifie si la méthode __str__ du modèle CartItem renvoie la représentation en chaîne du produit associé.
    """
    self.assertEqual(str(self.cart_item), str(self.cart_item.product))

  def test_cart_item_sub_total(self):
    """
    Vérifie si la méthode sub_total du modèle CartItem renvoie le montant total correct pour l'article de panier.
    """
    self.assertEqual(self.cart_item.sub_total(), self.cart_item.product.price * self.cart_item.quantity)

  def test_cart_item_is_active(self):
    """
    Vérifie si l'attribut is_active de l'article de panier est True.
    """
    self.assertTrue(self.cart_item.is_active)
  
  def test_cart_has_date_added(self):
    """
    Vérifie que le panier a un champ date_added correctement défini.
    """
    self.assertIsNotNone(self.cart.date_added)
  
  def test_cart_date_added_is_auto_now_add(self):
    """
    Vérifie que le champ date_added est automatiquement défini au moment de la création.
    """
    self.assertEqual(self.cart.date_added, date.today())
  
  def test_product_category(self):
    """
    Vérifie que le produit a une catégorie correctement définie.
    """
    self.assertEqual(self.product.category.category_name, 'test category')
  
  def test_product_price(self):
    """
    Vérifie que le produit a un prix correctement défini.
    """
    self.assertEqual(self.product.price, 10)
  
  def test_product_str(self):
    """
    Vérifie si la méthode __str__ du modèle Produit renvoie le nom du produit.
    """
    self.assertEqual(str(self.product), self.product.product_name)
  
  def test_cart_item_deletion(self):
    """
    Teste la suppression d'un article du panier.
    """
    initial_cart_item_count = CartItem.objects.count()
    self.cart_item.delete()
    final_cart_item_count = CartItem.objects.count()
    self.assertEqual(final_cart_item_count, initial_cart_item_count - 1)
  
  def test_cart_item_update(self):
    """
    Teste la mise à jour de la quantité d'un article dans le panier.
    """
    new_quantity = 5
    self.cart_item.quantity = new_quantity
    self.cart_item.save()
    updated_cart_item = CartItem.objects.get(id=self.cart_item.id)
    self.assertEqual(updated_cart_item.quantity, new_quantity)

  def test_cart_total_amount(self):
    """
    Teste le montant total du panier.
    """
    total = sum(item.sub_total() for item in self.cart.cartitem_set.all())
    self.assertEqual(total, self.cart_item.sub_total())

  def test_cart_item_quantity_increase(self):
    """
    Teste l'augmentation de la quantité d'un article du panier.
    """
    new_quantity = self.cart_item.quantity + 1
    self.cart_item.quantity = new_quantity
    self.cart_item.save()
    updated_cart_item = CartItem.objects.get(id=self.cart_item.id)
    self.assertEqual(updated_cart_item.quantity, new_quantity)

  def test_cart_item_quantity_decrease(self):
    """
    Teste la diminution de la quantité d'un article du panier.
    """
    if self.cart_item.quantity > 1:
      new_quantity = self.cart_item.quantity - 1
      self.cart_item.quantity = new_quantity
      self.cart_item.save()
      updated_cart_item = CartItem.objects.get(id=self.cart_item.id)
      self.assertEqual(updated_cart_item.quantity, new_quantity)

  def test_cart_item_multiple_products(self):
    """
    Teste l'ajout de plusieurs produits dans un article du panier.
    """
    second_product = Product.objects.create(product_name='Second test product', price=15, category=self.product.category, slug='second-test-product')
    CartItem.objects.create(product=second_product, cart=self.cart, quantity=2)
    self.assertEqual(CartItem.objects.filter(cart=self.cart).count(), 2)

  def test_cart_item_product_removal(self):
    """
    Teste la suppression d'un produit d'un article du panier.
    """
    initial_cart_item_count = CartItem.objects.filter(cart=self.cart).count()
    self.cart_item.delete()
    final_cart_item_count = CartItem.objects.filter(cart=self.cart).count()
    self.assertEqual(final_cart_item_count, initial_cart_item_count - 1)
