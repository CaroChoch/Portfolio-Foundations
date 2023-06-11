from django.db import models


class Category(models.Model):
  """
  Modèle représentant une catégorie.
  """
  category_name = models.CharField(max_length=50, unique=True)
  slug = models.SlugField(max_length=100, unique=True)
  description = models.TextField(max_length=255, blank=True)
  cat_image = models.ImageField(upload_to='photos/categories', blank=True)

  class Meta:
    """
    Classe Meta contenant les métadonnées pour le modèle Category.
    """
    verbose_name = 'category'
    verbose_name_plural = 'categories'

  def __str__(self):
    """
    Renvoie une représentation en chaîne de caractères du nom de la catégorie.
    """
    return self.category_name
