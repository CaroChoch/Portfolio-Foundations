from django.test import TestCase
from store.models import Product, Variation
from category.models import Category
from django.conf import settings
from django.core.exceptions import ValidationError


class ProductModelTest(TestCase):
  """
  Classe de test pour le modèle Store.
  """
  def setUp(self):
    """
    Crée une catégorie de test
    """
    category = Category.objects.create(category_name='Test category', slug='test-category')

    # Crée un produit de test avec une variation associée
    self.product = Product.objects.create(
      product_name='Test product',
      title_online='Test title',
      slug='test-product',
      description='Test description',
      price=10.0,
      stock=5,
      category=category
    )
    Variation.objects.create(
      product=self.product,
      variation_category='color',
      variation_value='Red',
      is_active=True
    )
  
  def test_product_creation(self):
    """
    Vérifie que le produit a été créé avec succès
    """
    self.assertTrue(isinstance(self.product, Product))
    self.assertEqual(str(self.product), 'Test product')

  def test_product_url(self):
    """
    Vérifie que la méthode get_url renvoie l'URL attendue pour le produit
    """
    expected_url = '/store/category/test-category/test-product/'
    self.assertEqual(self.product.get_url(), expected_url)

  def test_product_has_name(self):
    """
    Vérifie que le produit a un nom correctement défini
    """
    self.assertEqual(self.product.product_name, 'Test product')
  
  def test_product_has_title_online(self):
    """
    Vérifie que le produit a un titre en ligne correctement défini
    """
    self.assertEqual(self.product.title_online, 'Test title')
  
  def test_product_has_slug(self):
    """
    Vérifie que le produit a un slug correctement défini
    """
    self.assertEqual(self.product.slug, 'test-product')
  
  def test_product_has_description(self):
    """
    Vérifie que le produit a une description correctement définie
    """
    self.assertEqual(self.product.description, 'Test description')
  
  def test_product_has_price(self):
    """
    Vérifie que le produit a un prix correctement défini
    """
    self.assertEqual(self.product.price, 10.0)
  
  def test_product_has_positive_price(self):
    """
    Vérifie que le prix du produit est positif
    """
    self.assertGreater(self.product.price, 0)
  
  def test_product_has_valid_stock(self):
    """
    Vérifie que le stock du produit est un nombre positif
    """
    self.assertGreater(self.product.stock, 0)
  
  def test_product_has_stock(self):
    """
    Vérifie que le produit a un stock correctement défini
    """
    self.assertEqual(self.product.stock, 5)
  
  def test_product_is_available(self):
    """
    Vérifie que le produit est disponible (par défaut, True)
    """
    self.assertTrue(self.product.is_available)

  def test_product_has_category(self):
    """
    Vérifie que le produit a une catégorie associée correctement définie
    """
    category = Category.objects.get(category_name='Test category')
    self.assertEqual(self.product.category, category)
  
  def test_product_has_created_date(self):
    """
    Vérifie que le produit a une date de création définie
    """
    self.assertIsNotNone(self.product.created_date)
  
  def test_product_has_modified_date(self):
    """
    Vérifie que le produit a une date de modification définie
    """
    self.assertIsNotNone(self.product.modified_date)
  
  def test_product_variation_count(self):
    """
    Vérifie le nombre de variations associées au produit (dans cet exemple, une variation)
    """
    self.assertEqual(self.product.variation_set.count(), 1)
  
  def test_product_str(self):
    """
    Vérifie si la méthode __str__ du modèle Product renvoie le nom du produit
    """
    self.assertEqual(str(self.product), 'Test product')
  
  def test_product_has_images(self):
    """
    Vérifie si le produit a des images correctement configurées.
    """
    image_path = 'photos/products/test-product.jpg'
    self.product.images.name = image_path
    self.product.save()
    self.assertEqual(self.product.images.path, f'{settings.MEDIA_ROOT}/{image_path}')
    self.assertEqual(self.product.images.url, f'{settings.MEDIA_URL}{image_path}')

  def test_product_has_no_second_image(self):
    """
    Vérifie que le produit n'a pas de deuxième image
    """
    self.assertFalse(self.product.second_image)

  def test_product_get_url(self):
    """
    Vérifie que la méthode get_url renvoie l'URL correcte pour le produit
    """
    expected_url = '/store/category/test-category/test-product/'
    self.assertEqual(self.product.get_url(), expected_url)

  def test_product_variation_category_choices(self):
    """
    Vérifie que la variation_category n'accepte que les choix valides
    """
    invalid_variation = Variation.objects.create(
        product=self.product,
        variation_category='invalid_category',
        variation_value='Value',
        is_active=True
    )
    with self.assertRaises(ValidationError) as context:
        invalid_variation.clean_fields()
    exception_message = str(context.exception)
    self.assertIn("invalid_category", exception_message)
