from django.db import models
from django.urls import reverse


GENDER_CHOICES = [
    ('H', 'Homme'),
    ('F', 'Femme'),
    ('O', 'Autre'),
]

PRODUCT_TYPE_CHOICES = [
    ('Y', 'Accessoires Homme'),
    ('X', 'Accessoires Femme'),
    ('A', 'Vêtements Homme'),
    ('B', 'Vêtements Femme'),
    ('O', 'Autre'),
]


class Category(models.Model):
    """
    Modèle représentant une catégorie.
    """
    category_name   = models.CharField(max_length=50, unique=True)
    category_online = models.CharField(max_length=50, default="")
    slug            = models.SlugField(max_length=100, unique=True)
    description     = models.TextField(max_length=255, blank=True)
    cat_image       = models.ImageField(upload_to='photos/categories', blank=True)
    gender          = models.CharField(max_length=1, choices=GENDER_CHOICES, default="")
    product_type    = models.CharField(max_length=1, choices=PRODUCT_TYPE_CHOICES, default="")


    class Meta:
        """
        Classe Meta contenant les métadonnées pour le modèle Category.
        """
        verbose_name        = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        """
        Renvoie une représentation en chaîne de caractères du nom de la catégorie.
        """
        return self.category_name
