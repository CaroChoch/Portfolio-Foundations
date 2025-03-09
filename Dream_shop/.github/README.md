# GitHub Actions pour Dream Shop

Ce dossier contient les workflows GitHub Actions configurés pour le projet Dream Shop.

## Workflows disponibles

### 1. Django CI (`django-ci.yml`)

Ce workflow est exécuté à chaque push ou pull request sur les branches `main` ou `master`. Il réalise les tâches suivantes :

- **Tests** : Exécute les tests Django pour vérifier que le code fonctionne correctement

### 2. Docker CI (`docker-ci.yml`)

Ce workflow est exécuté à chaque push ou pull request sur les branches `main` ou `master`. Il réalise les tâches suivantes :

- Construction de l'image Docker
- Test de l'image Docker

## Configuration requise

Pour que ces workflows fonctionnent correctement, vous devez configurer les secrets GitHub suivants :

- `SECRET_KEY` : La clé secrète Django (optionnel pour les tests)

## Comment exécuter les tests localement

Pour exécuter les mêmes tests localement avant de pousser vos modifications :

```bash
# Tests Django
python manage.py test

# Tests Docker
docker build -t dreamshop:test .
docker run --rm dreamshop:test python -m pytest -xvs
``` 