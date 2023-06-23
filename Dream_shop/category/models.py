from django.db import models
from django.urls import reverse

# Les choix pour le champ de genre.
GENDER_CHOICES = [
    ('H', 'Homme'),
    ('F', 'Femme'),
    ('O', 'Autre'),
]

# Les choix pour le champ de type de produit.
PRODUCT_TYPE_CHOICES = [
    ('Y', 'Accessoires Homme'),
    ('X', 'Accessoires Femme'),
    ('A', 'Vêtements Homme'),
    ('B', 'Vêtements Femme'),
    ('O', 'Autre'),
]

class Category(models.Model):
    """
    Modèle Django représentant une catégorie de produits.

    Champs:
    - category_name: Le nom de la catégorie.
    - category_online: Champ inutilisé dans le code actuel, peut-être prévu pour des usages futurs.
    - slug: L'identifiant unique pour la catégorie utilisé dans les URLs.
    - description: Une description détaillée de la catégorie.
    - cat_image: L'image associée à la catégorie.
    - gender: Le genre auquel la catégorie est associée (Homme, Femme ou Autre).
    - product_type: Le type de produits que contient la catégorie (Vêtements ou Accessoires pour Homme ou Femme).
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

        Attributs:
        - verbose_name: Le nom en lecture facile pour le modèle.
        - verbose_name_plural: Le nom en lecture facile pour le modèle au pluriel.
        """
        verbose_name        = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        """
        Méthode pour obtenir l'URL de la vue des produits par catégorie pour cette catégorie.

        Retourne:
        L'URL de la vue des produits par catégorie pour cette catégorie.
        """
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        """
        Méthode pour obtenir une représentation sous forme de chaîne de caractères de l'objet Category.

        Retourne:
        Le nom de la catégorie.
        """
        return self.category_name