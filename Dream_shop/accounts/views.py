from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def register(request):
  """
  Gère l'enregistrement d'un nouvel utilisateur.

  Si la méthode de la requête est POST, cette fonction récupère les données du formulaire d'inscription à partir de la requête,
  puis valide le formulaire. Si le formulaire est valide, un nouvel utilisateur est créé et sauvegardé en base de données,
  un message de succès est affiché à l'utilisateur et une réponse JSON indiquant le succès est renvoyée.
  Si le formulaire n'est pas valide, une réponse JSON indiquant l'échec et contenant les erreurs de formulaire est renvoyée.

  Si la méthode de la requête n'est pas POST (par exemple, GET), cette fonction crée un nouveau formulaire d'inscription vide
  et renvoie la page d'inscription avec ce formulaire.

  Args:
    request (HttpRequest): La requête HTTP reçue.

  Returns:
    HttpResponse: La réponse HTTP à renvoyer au client.
  """
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      civility         = form.cleaned_data['civility']
      first_name       = form.cleaned_data['first_name']
      last_name        = form.cleaned_data['last_name']
      address          = form.cleaned_data['address']
      postal_code      = form.cleaned_data['postal_code']
      city             = form.cleaned_data['city']
      country          = form.cleaned_data['country']
      email            = form.cleaned_data['email']
      phone_number     = form.cleaned_data['phone_number']
      birth_date       = form.cleaned_data['birth_date']
      password         = form.cleaned_data['password']
      confirm_password = form.cleaned_data['confirm_password']
      username         = email.split("@")[0]

      user = Account.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        email=email,
        username=username,
        password=password,
      )
      user.phone_number = phone_number
      user.address = address
      user.postal_code = postal_code
      user.birth_date = birth_date
      user.city = city
      user.country = country
      user.civility = civility
      user.save()
      messages.success(request, 'Inscription confirmée.')
      return JsonResponse({'success': True})
    else:
      errors = form.errors.as_json()
      return JsonResponse({'success': False, 'errors': errors}, status=400)
  else:
    form = RegistrationForm()


  context = {
    'form': form,
  }
  return render(request, 'accounts/register.html', context)


def login(request):
  """
  Gère la connexion d'un utilisateur.

  Si la méthode de la requête est POST, cette fonction récupère l'e-mail et le mot de passe de l'utilisateur à partir de la requête,
  puis tente d'authentifier l'utilisateur. Si l'utilisateur est authentifié avec succès, il est connecté et redirigé vers la page d'accueil.
  Sinon, un message d'erreur est affiché à l'utilisateur et il est redirigé vers la page de connexion.

  Si la méthode de la requête n'est pas POST (par exemple, GET), cette fonction renvoie simplement la page de connexion.

  Args:
    request (HttpRequest): La requête HTTP reçue.

  Returns:
    HttpResponse: La réponse HTTP à renvoyer au client.
  """
  if request.method == 'POST':
    email = request.POST['email']
    password = request.POST['password']

    user = auth.authenticate(email=email, password=password)

    if user is not None:
      auth.login(request, user)
      #messages.success(request, "Vous êtes bien connecté !")
      return redirect('home')
    else:
      messages.error(request, "Identification échouée, veuillez vérifier vos identifiants !")
      return redirect('login')

  return render(request, 'accounts/login.html')


@login_required(login_url = 'login')
def logout(request):
  """
  Gère la déconnexion d'un utilisateur.

  Cette fonction déconnecte l'utilisateur et affiche un message de succès,
  puis redirige l'utilisateur vers la page de connexion.

  Cette fonction nécessite que l'utilisateur soit connecté (déterminé par le décorateur login_required).

  Args:
    request (HttpRequest): La requête HTTP reçue.

  Returns:
    HttpResponse: La réponse HTTP à renvoyer au client.
  """
  auth.logout(request)
  messages.success(request, 'Vous êtes bien déconnecté !')
  return redirect('login')
