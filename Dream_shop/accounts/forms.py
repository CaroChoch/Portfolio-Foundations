from django import forms
from .models import Account
from django.contrib.auth.validators import ASCIIUsernameValidator, UnicodeUsernameValidator
from django.core.validators import MinLengthValidator, RegexValidator


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Mot de passe',
        widget=forms.PasswordInput,
        validators=[
            # Minimum de 8 caractères
            MinLengthValidator(8),
            # Doit contenir au moins une lettre
            RegexValidator(
                regex=r'[a-zA-Z]',
                message="Le mot de passe doit contenir au moins une lettre.",
                code='password_no_letter'
            ),
            # Doit contenir au moins un chiffre
            RegexValidator(
                regex=r'[0-9]',
                message="Le mot de passe doit contenir au moins un chiffre.",
                code='password_no_digit'
            ),
            # Doit contenir au moins un caractère spécial
            RegexValidator(
                regex=r'[!@#$%^&*()]',
                message="Le mot de passe doit contenir au moins un caractère spécial.",
                code='password_no_special'
            ),
        ]
    )
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=Account.GENDER_CHOICES)


    class Meta:
        model = Account
        fields = ['gender', 'last_name', 'first_name', 'address', 'postal_code', 'city', 'country','email', 'phone_number', 'birth_date', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and len(password) < 8:
            raise forms.ValidationError("Le mot de passe doit contenir au moins 8 caractères.")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError(
                "Les deux mots de passe ne sont pas identiques !"
            )

        # Validation de l'adresse email
        email = cleaned_data.get('email')
        if email and Account.objects.filter(email=email).exists():
            raise forms.ValidationError("Cette adresse e-mail existe déjà.")

        return cleaned_data

    
