from django import forms
from .models import Account
import re
import requests
from datetime import date, timedelta, datetime
from django.utils.translation import gettext_lazy as _


class RegistrationForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	confirm_password = forms.CharField(widget=forms.PasswordInput())
	
	birth_date = forms.DateField(
		widget=forms.DateInput(
			format='%d/%m/%Y',
    ),
    input_formats=('%d/%m/%Y',)
  )


	class Meta:
		model = Account
		fields = ['civility', 'first_name', 'last_name', 'address', 'postal_code', 'city', 'country', 'email', 'phone_number', 'birth_date', 'password', 'confirm_password']


	def clean(self):
		cleaned_data = super(RegistrationForm, self).clean()
		password = cleaned_data.get('password')
		confirm_password = cleaned_data.get('confirm_password')

		if password != confirm_password:
			raise forms.ValidationError("Les deux mots de passe ne sont pas identiques !")

		if len(password) < 8:
			raise forms.ValidationError("Le mot de passe doit contenir au moins 8 caractères.")
		
		if not any(char.isalpha() for char in password):
			raise forms.ValidationError("Le mot de passe doit contenir au moins une lettre.")
		
		if not any(char.isupper() for char in password):
			raise forms.ValidationError("Le mot de passe doit contenir au moins une lettre majuscule.")
		
		if not any(char.isdigit() for char in password):
			raise forms.ValidationError("Le mot de passe doit contenir au moins un chiffre.")
		
		if not any(char in '!@#$%^&*()' for char in password):
			raise forms.ValidationError("Le mot de passe doit contenir au moins un caractère spécial.")


	def clean_postal_code(self):
		postal_code = self.cleaned_data.get('postal_code')

		if len(postal_code) != 5 or not postal_code.isdigit():
			raise forms.ValidationError('Veuillez entrer un code postal valide.')
		return postal_code

	def clean_phone_number(self):
		phone_number = self.cleaned_data.get('phone_number')
		# Supprimez les caractères non numériques du numéro de téléphone
		phone_number = re.sub(r'\D', '', phone_number)

		if not phone_number.isdigit():
			raise forms.ValidationError("Le numéro de téléphone ne doit contenir que des chiffres.")
		
		if len(phone_number) != 10:
			raise forms.ValidationError("Le numéro de téléphone doit comporter 10 chiffres.")

		return phone_number


	def clean_birth_date(self):
		birth_date = self.cleaned_data.get('birth_date')
		today = date.today()
		age_limit = today - timedelta(days=365 * 18)  # Âge minimum de 18 ans

		if birth_date > today:
			raise forms.ValidationError("La date de naissance ne peut pas être dans le futur.")

		if birth_date > age_limit:
			raise forms.ValidationError("Vous devez avoir au moins 18 ans pour vous inscrire.")

		return birth_date
