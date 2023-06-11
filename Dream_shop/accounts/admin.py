# Importe le module admin pour interagir avec l'administration de Django.
from django.contrib import admin
# Importe la classe UserAdmin fournie par Django pour la personnalisation de l'administration d'utilisateur.
from django.contrib.auth.admin import UserAdmin
from .models import Account


# Définit une classe AccountAdmin qui étend UserAdmin.
# Cela nous permet de personnaliser l'apparence et le comportement de l'administration pour le modèle Account.
class AccountAdmin(UserAdmin):
  """
  Classe personnalisée pour l'administration des utilisateurs Account.
  """
  list_display       = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
  list_display_links = ('email', 'first_name', 'last_name')
  readonly_fields    = ('last_login', 'date_joined')
  ordering           = ('-date_joined',)

  filter_horizontal = ()
  list_filter       = ()
  fieldsets         = ()

# Enregistre le modèle Account avec l'administration de Django en utilisant la classe AccountAdmin personnalisée.
admin.site.register(Account, AccountAdmin)
