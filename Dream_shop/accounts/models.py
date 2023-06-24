from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime


class MyAccountManager(BaseUserManager):
  """
  Gestionnaire personnalisé pour le modèle Account.
  """
  def create_user(self, first_name, last_name, username, email, password=None):
    """
    Crée et sauvegarde un utilisateur standard avec les champs spécifiés.
    """
    if not email:
      raise ValueError('User must have an email address')
    
    if not username:
      raise ValueError('User must have an username')
    
    user = self.model(
      email      = self.normalize_email(email),
      username   = username,
      first_name = first_name,
      last_name  = last_name,
    )

    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_superuser(self, first_name, last_name, email, username, password):
    """
    Crée et sauvegarde un superutilisateur avec tous les droits d'administration.
    """
    user = self.create_user(
      email      = self.normalize_email(email),
      username   = username,
      password   = password,
      first_name = first_name,
      last_name  = last_name,
    )
    user.is_admin      = True
    user.is_active     = True
    user.is_staff      = True
    user.is_superadmin = True
    user.save(using=self._db)
    return user


class Account(AbstractBaseUser):
  """
  Modèle de compte utilisateur personnalisé.
  """
  GENDER_CHOICES = (
    ('F', 'Madame'),
    ('M', 'Monsieur'),
  )

  first_name   = models.CharField(max_length=50)
  last_name    = models.CharField(max_length=50)
  username     = models.CharField(max_length=50, unique=True)
  email        = models.EmailField(max_length=100, unique=True)
  phone_number = models.CharField(max_length=50)
  gender       = models.CharField(max_length=1, choices=GENDER_CHOICES)
  address      = models.CharField(max_length=100, default='')
  postal_code  = models.CharField(max_length=20, default='N/A')
  city         = models.CharField(max_length=50, default="Unknown")
  country      = models.CharField(max_length=50, default="Unknown")
  birth_date   = models.DateField(default=datetime.date.today)
    
  # Ces champs sont requis pour la gestion des utilisateurs dans Django
  date_joined      = models.DateTimeField(auto_now_add=True)
  last_login       = models.DateTimeField(auto_now_add=True)
  is_admin         = models.BooleanField(default=False)
  is_staff         = models.BooleanField(default=False)
  is_active        = models.BooleanField(default=False)
  is_superadmin    = models.BooleanField(default=False)

  # Définition du champ utilisé comme identifiant pour ce modèle d'utilisateur
  USERNAME_FIELD  = 'email'
  # Champs requis lors de la création d'un utilisateur
  REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

  # Lien du modèle d'utilisateur avec le gestionnaire créé précédemment
  objects = MyAccountManager()

  def __str__(self):
    """
    Renvoie une représentation en chaîne de caractères de l'instance de modèle Account.
    """
    return self.email

  def has_perm(self, perm, obj=None):
    """
    Vérifie si l'utilisateur a une permission spécifique.
    """
    return self.is_admin

  def has_module_perms(self, add_label):
    """
    Vérifie si l'utilisateur a des permissions sur un module spécifique.
    """
    return True
