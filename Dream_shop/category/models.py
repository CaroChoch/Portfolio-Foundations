from django.db import models

# Create your models here.

# Définition de la classe Category qui hérite de models.Model
class Category(models.Model):
  category_name = models.CharField(max_length=50, unique=True)
  slug = models.CharField(max_length=100, unique=True)
  description = models.TextField(max_length=255, blank=True)
  cat_image = models.ImageField(upload_to='photos/categories', blank=True)

  # La classe Meta est une classe imbriquée qui contient des métadonnées pour le modèle.
  class Meta:
    verbose_name = 'category'
    verbose_name_plural = 'categories'

  # La méthode __str__ est utilisée pour représenter l'objet Category sous forme de chaîne.
  def __str__(self):
    return self.category_name
