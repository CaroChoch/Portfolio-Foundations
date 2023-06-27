from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage, send_mail


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

      # USER ACTIVATION
      current_site = get_current_site(request)
      mail_subject = "Votre compte Ma Boutique de rêve a été créé ! Merci de confirmer votre adresse mail."
      message = render_to_string('accounts/account_verification_email.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
      })
      to_email = email
      send_mail(mail_subject, message, None, [to_email])
      messages.success(request, 'Merci pour votre inscription. Pour la confirmer, veuillez cliquer sur le lien de confirmation envoyé par mail.')
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
      #messages.success(request, "Vous êtes bien connecté !")
      return redirect('home')
    else:
      messages.error(request, "Identification échouée, veuillez vérifier vos identifiants !")
      return redirect('login')

  return render(request, 'accounts/login.html')

@login_required(login_url = 'login')
def logout(request):
  auth.logout(request)
  messages.success(request, 'Vous êtes bien déconnecté !')
  return redirect('login')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account.objects.get(pk=uid)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Votre compte a été activé avec succès.")
            return redirect('login')
        else:
            messages.error(request, "Le lien d'activation est invalide.")
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        messages.error(request, "Le lien d'activation est invalide.")
    
    return redirect('home')
