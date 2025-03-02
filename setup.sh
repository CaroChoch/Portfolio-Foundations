#!/bin/bash

echo "🚀 Création de l'environnement virtuel..."
python3 -m venv venv

# Activation de l'environnement virtuel
echo "🔌 Activation de l'environnement virtuel..."
source venv/bin/activate

# Installation des dépendances
echo "📦 Installation des dépendances..."
pip install -r requirements.txt

# Création de la base de données MySQL
echo "🗄️ Création de la base de données MySQL..."
if mysql -u root -p <<EOF
CREATE DATABASE IF NOT EXISTS db_dream_shop CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EOF
then
    echo "✅ Base de données 'db_dream_shop' créée avec succès !"
else
    echo "❌ Erreur lors de la création de la base de données."
    exit 1
fi

# Importation des données dans la base de données
echo "📥 Importation des données dans la base de données..."
if mysql -u root -p db_dream_shop < Dream_shop/db_dream_shop_dump.sql
then
    echo "✅ Données importées avec succès dans 'db_dream_shop' !"
else
    echo "❌ Erreur lors de l'importation des données."
    exit 1
fi

# Configuration de Django
echo "⚙️ Configuration de Django..."
cd Dream_shop
python manage.py makemigrations
python manage.py migrate

# Création du superuser
echo "👤 Création du compte administrateur..."
echo "Voulez-vous créer un compte administrateur ? (o/n)"
read reponse
if [ "$reponse" = "o" ] || [ "$reponse" = "O" ]; then
    python manage.py createsuperuser
    echo "✅ Compte administrateur créé avec succès !"
fi

# Message de confirmation
echo "
✨ Installation terminée avec succès ! ✨

Pour utiliser l'application :
🎯 1. Activez l'environnement virtuel : source venv/bin/activate
🎯 2. Allez dans le dossier du projet : cd Dream_shop
🎯 3. Lancez le serveur : python manage.py runserver
🎯 4. Accédez à l'interface d'administration : http://127.0.0.1:8000/admin

Bon développement ! 🚀" 