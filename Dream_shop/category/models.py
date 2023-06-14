from django.db import models

GENDER_CHOICES = [
    ('H', 'Homme'),
    ('F', 'Femme'),
    ('X', 'Autre'),
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

    class Meta:
        """
        Classe Meta contenant les métadonnées pour le modèle Category.
        """
        verbose_name        = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        """
        Renvoie une représentation en chaîne de caractères du nom de la catégorie.
        """
        return self.category_name


class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    category_online = models.CharField(max_length=50, default="")

    class Meta:
        ordering = ['name',] # ordre alphabetique

    def __str__(self):
        return self.name
