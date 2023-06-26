from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def register(request):
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
      return JsonResponse({'success': False, 'errors': errors})
  else:
    form = RegistrationForm()


  context = {
    'form': form,
  }
  return render(request, 'accounts/register.html', context)


def login(request):
  if request.method == 'POST':
    email = request.POST['email']
    password = request.POST['password']

    user = auth.authenticate(email=email, password=password)

    if user is not None:
      auth.login(request, user)
      #messages.success(request, 'Vous êtes bien connecté !')
      return redirect('home')
    else:
      messages.error(request,'Identification échouée. Veuillez vérifier vos identifiants !')
      return redirect('login')

  return render(request, 'accounts/login.html')

@login_required(login_url = 'login')
def logout(request):
  auth.logout(request)
  messages.success(request, 'Vous êtes bien déconnecté !')
  return redirect('login')
