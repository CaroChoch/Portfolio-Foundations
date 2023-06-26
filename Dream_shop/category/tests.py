from django.test import TestCase
from category.models import Category
from django.urls import reverse
import os


class CategoryModelTest(TestCase):
  """
  Classe de test pour le modèle Category.
  """
  def setUp(self):
    """
    Crée une catégorie de test avant chaque test.
    """
    self.category = Category.objects.create(category_name='Test category', slug='test-category')

  def test_category_creation(self):
    """
    Vérifie que nous pouvons créer une catégorie et que sa représentation sous forme de chaîne est correcte.
    """
    self.assertTrue(isinstance(self.category, Category))
    self.assertEqual(str(self.category), 'Test category')
  
  def test_category_url(self):
    """
    Vérifie que la méthode get_url renvoie l'URL attendue pour la catégorie.
    """
    expected_url = '/store/category/test-category/'
    self.assertEqual(self.category.get_url(), expected_url)
  
  def test_category_has_name(self):
    """
    Vérifie que la catégorie a un nom correctement défini.
    """
    self.assertEqual(self.category.category_name, 'Test category')
  
  def test_category_has_slug(self):
    """
    Vérifie que la catégorie a un slug correctement défini.
    """
    self.assertEqual(self.category.slug, 'test-category')

  def test_category_has_description(self):
    """
    Vérifie que la catégorie a une description correctement définie.
    """
    self.assertEqual(self.category.description, '')
  
  def test_category_has_image(self):
    """
    Vérifie que la catégorie a une image correctement définie.
    """
    self.assertEqual(self.category.cat_image, '')
  
  def test_category_has_gender(self):
    """
    Vérifie que la catégorie a un genre correctement défini.
    """
    self.assertEqual(self.category.gender, '')
  
  def test_category_has_product_type(self):
    """
    Vérifie que la catégorie a un type de produit correctement défini.
    """
    self.assertEqual(self.category.product_type, '')
  
  def test_category_str(self):
    """
    Vérifie si la méthode __str__ du modèle Category renvoie le nom de la catégorie.
    """
    self.assertEqual(str(self.category), 'Test category')
  
  def test_category_get_url(self):
    """
    Vérifie si la méthode get_url renvoie l'URL correcte pour la catégorie.
    """
    expected_url = reverse('products_by_category', args=[self.category.slug])
    self.assertEqual(self.category.get_url(), expected_url)
  
  def test_category_online_default_value(self):
    """
    Vérifie que le champ category_online a la valeur par défaut vide.
    """
    self.assertEqual(self.category.category_online, '')

  def test_category_description_blank(self):
    """
    Vérifie que le champ description peut être vide.
    """
    category = Category.objects.create(category_name='Empty category', slug='empty-category', description='')
    self.assertEqual(category.description, '')

  def test_category_gender_choices(self):
    """
    Vérifie que le champ gender n'accepte que les choix valides.
    """
    valid_gender_category = Category()
    valid_gender_category.category_name = 'Valid gender'
    valid_gender_category.slug = 'valid-gender'
    valid_gender_category.gender = 'H'
    valid_gender_category.category_online = 'Online'
    valid_gender_category.product_type = 'A'
    valid_gender_category.clean_fields()

  def test_category_product_type_choices(self):
    """
    Vérifie que le champ product_type n'accepte que les choix valides.
    """
    valid_product_type_category = Category()
    valid_product_type_category.category_name = 'Valid product type'
    valid_product_type_category.slug = 'valid-product-type'
    valid_product_type_category.gender = 'H'
    valid_product_type_category.product_type = 'A'
    valid_product_type_category.category_online = 'Online'
    valid_product_type_category.clean_fields()

  def test_category_description_max_length(self):
    """
    Vérifie que la longueur maximale de la description de catégorie est respectée.
    """
    max_length = Category._meta.get_field('description').max_length
    category = Category.objects.create(
        category_name='Max length description',
        slug='max-length-description',
        description='a' * max_length
    )
    self.assertEqual(len(category.description), max_length)


  def test_category_image_upload(self):
      """
      Vérifie que l'upload d'image pour une catégorie fonctionne correctement.
      """
      image_path = 'path/to/image.jpg'
      category = Category.objects.create(
          category_name='Image upload',
          slug='image-upload',
          cat_image=image_path
      )
      expected_filename = os.path.basename(image_path)
      self.assertIn(expected_filename, category.cat_image.path)
