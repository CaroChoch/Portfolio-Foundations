from django.db import models
from category.models import Category

class Product(models.Model):
    """
    Modèle représentant un produit dans le système.
    """
    product_name = models.CharField(max_length=200, unique=True)                         # Nom du produit (champ texte limité à 200 caractères), doit être unique
    title_online = models.CharField(max_length=200, default='')                          # Titre du produit qui sera en ligne
    slug = models.SlugField(max_length=200, unique=True)                                 # Slug pour l'URL conviviale du produit (champ texte limité à 200 caractères), doit être unique
    description = models.TextField(max_length=500, blank=True)                           # Description du produit (champ texte avec une limite de 500 caractères), peut être vide
    price = models.FloatField(default=0.0)                                               # Prix du produit (champ entier)
    images = models.ImageField(upload_to='photos/products', blank=True, null=True)       # Images du produit (champ pour télécharger une image, stockée dans le répertoire 'photos/products')
    second_image = models.ImageField(upload_to='photos/products', blank=True, null=True) # Seconde image pour le reverse des produits de la collection complète
    stock = models.IntegerField(default=0)                                               # Stock disponible du produit (champ entier)
    is_available = models.BooleanField(default=True)                                     # Indicateur de disponibilité du produit (champ booléen avec valeur par défaut True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)                     # Catégorie du produit (relation ForeignKey avec le modèle Category, suppression en cascade en cas de suppression de la catégorie)
    created_date = models.DateTimeField(auto_now_add=True)                               # Date de création du produit (remplie automatiquement lors de la création)
    modified_date = models.DateTimeField(auto_now=True)                                  # Date de modification du produit (mise à jour automatique lors de chaque modification)
    

    def __str__(self):
        """
        Renvoie une représentation en chaîne de caractères du produit.
        """
        return self.product_name
