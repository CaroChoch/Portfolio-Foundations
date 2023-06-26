from django.test import TestCase, Client
from django.urls import reverse
from .models import Account
from .forms import RegistrationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required


class AccountModelTest(TestCase):
  """
  Teste les fonctionnalités du modèle Account
  """
  def setUp(self):
    """
    Crée un nouvel utilisateur avant chaque test
    """
    self.account1 = Account.objects.create_user(first_name='test', last_name='user', email='test#user.com', username='testuser', password='password')
  
  def test_account_creation(self):
    """
    Vérifie si le compte utilisateur a été créé avec succès.
    """
    self.assertEqual(Account.objects.count(), 1)

  def test_account_str(self):
    """
    Vérifie si la méthode __str__ du modèle Account renvoie l'adresse e-mail de l'utilisateur.
    """
    self.assertEqual(str(self.account1), 'test#user.com') 



class RegistrationFormTest(TestCase):
  """
  Teste les fonctionnalités du formulaire d'inscription
  """
  def test_form_validity(self):
    """
    Vérifie si le formulaire d'inscription est valide avec des données correctes.
    """
    form = RegistrationForm(data={
      'civility': 'M',
      'first_name': 'test',
      'last_name': 'user',
      'address': '123 street',
      'postal_code': '12345',
      'city': 'test city',
      'country': 'test country',
      'email': 'test@user.com',
      'phone_number': '1234567890',
      'birth_date': '01/01/2000',
      'password': 'Password123!',
      'confirm_password': 'Password123!'
    })
    self.assertTrue(form.is_valid())



class AccountViewTest(TestCase):
  """
  Teste les vues de l'application accounts
  """
  def setUp(self):
    """
    Définit les URL et initialise un client de test avant chaque test
    """
    self.client = Client()
    self.register_url = reverse('register')
    self.login_url = reverse('login')
    self.logout_url = reverse('logout')

  def test_register_view(self):
    """
    Vérifie que la vue d'inscription fonctionne correctement avec des données correctes
    """
    response = self.client.post(self.register_url, {
      'civility': 'M',
      'first_name': 'test',
      'last_name': 'user',
      'address': '123 street',
      'postal_code': '12345',
      'city': 'test city',
      'country': 'test country',
      'email': 'test@user.com',
      'phone_number': '1234567890',
      'birth_date': '01/01/2000',
      'password': 'Password123!',
      'confirm_password': 'Password123!'
    }, format='json')
    self.assertEqual(response.status_code, 200)
  
  def test_login_view(self):
    """
    Vérifie que la vue de connexion fonctionne correctement avec des identifiants valides
    """
    Account.objects.create_user(first_name='test', last_name='user', email='test@user.com', username='testuser', password='password')
    response = self.client.post(self.login_url, {'email': 'test@user.com', 'password': 'password'}, format='json')
    self.assertEqual(response.status_code, 302)
  
  def test_logout_view(self):
    """
    Vérifie que la vue de déconnexion fonctionne correctement
    """
    Account.objects.create_user(first_name='test', last_name='user', email='test@user.com', username='testuser', password='password')
    self.client.login(email='test@user.com', password='password')
    response = self.client.get(self.logout_url)
    self.assertEqual(response.status_code, 302)
    user = auth.get_user(self.client)
    self.assertFalse(user.is_authenticated)
  
  def test_register_view_get(self):
    """
    Vérifie que la vue d'inscription renvoie un code 200 pour une requête GET
    """
    response = self.client.get(self.register_url)
    self.assertEqual(response.status_code, 200)
  
  def test_login_view_get(self):
    """
    Vérifie que la vue de connexion renvoie un code 200 pour une requête GET
    """
    response = self.client.get(self.login_url)
    self.assertEqual(response.status_code, 200)
  
  def test_logout_view_unauthenticated(self):
    """
    Vérifie que la vue de déconnexion renvoie un code 302 si l'utilisateur n'est pas connecté
    """
    response = self.client.get(self.logout_url)
    self.assertEqual(response.status_code, 302)
  
  def test_register_view_invalid_post(self):
    """
    Vérifie que la vue d'inscription renvoie un code 400 pour une requête POST invalide
    """
    response = self.client.post(self.register_url, {
      'civility': 'M',
      'first_name': 'test',
      'last_name': 'user',
      'address': '123 street',
      'postal_code': '1234',
      'city': 'test city',
      'country': 'test country',
      'email': 'invalid.com',
      'phone_number': '123456789',
      'birth_date': '01-01-2000',
      'password': 'Password123',
      'confirm_password': 'Password123'
    }, format='json')
    self.assertEqual(response.status_code, 400)

  def test_login_view_invalid_post(self):
    """
    Vérifie que la vue de connexion renvoie une redirection code 302 pour une requête POST invalide
    """
    response = self.client.post(self.login_url, {
      'email': 'test@user.com',
      'password': 'incorrect_password',
    }, format='json')
    self.assertEqual(response.status_code, 302)

  def test_logout_view_not_found(self):
    """
    Vérifie que la vue de déconnexion renvoie un code 404 pour une requête GET sur une URL inexistante
    """
    response = self.client.get('/accounts/logout/invalid/')
    self.assertEqual(response.status_code, 404)
  
  def test_register_view_not_found(self):
    """
    Vérifie que la vue d'inscription renvoie un code 404 pour une requête GET sur une URL inexistante
    """
    response = self.client.get('/accounts/register/invalid/')
    self.assertEqual(response.status_code, 404)

  def test_login_view_not_found(self):
    """
    Vérifie que la vue de connexion renvoie un code 404 pour une requête GET sur une URL inexistante
    """
    response = self.client.get('/accounts/login/invalid/')
    self.assertEqual(response.status_code, 404)

  def test_logout_view_authenticated(self):
    """
    Vérifie que la vue de déconnexion renvoie un code 302 si l'utilisateur est connecté
    """
    Account.objects.create_user(
        first_name='test',
        last_name='user',
        email='test@user.com',
        username='testuser',
        password='password'
    )
    self.client.login(email='test@user.com', password='password')
    response = self.client.get(self.logout_url)
    self.assertEqual(response.status_code, 302)
