from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages
from django.http import JsonResponse


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
  return render(request, 'accounts/login.html')

def logout(request):
  return
