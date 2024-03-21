# Documentation de l'API FastAPI 🚀

Cette API permet la gestion des utilisateurs et de leurs ressources dans une application, en utilisant des technologies de pointe comme SQLAlchemy, Pydantic, et Passlib, avec Alembic pour les migrations de base de données et PostgreSQL comme système de gestion de base de données.

## 🛠 Configuration de l'environnement

Assurez-vous que PostgreSQL est installé et configuré sur votre machine. Une base de données dédiée à cette application est requise pour une utilisation optimale.

Le projet comporte un environnement virtuel qui isole les dépendances du projet. Voici comment l'activer et installer toutes les dépendances nécessaires :

#### Pour les utilisateurs Windows

```powershell

# Ouvrir un terminal powershell à la racine du projet
# Activer l'environnement virtuel
.\env\Scripts\Activate.ps1

# Installer les dépendances
pip install -r requirements.txt

# Créer une migration
alembic revision --autogenerate -m "First migration"

# Appliquer les migrations
alembic upgrade head

```

## 📚 Modèles de données

Les modèles sont définis dans `sql_app/models.py`, créant un lien direct avec les tables PostgreSQL :

- **User**: Gère les informations des utilisateurs.
- **Ressource**: Gère les ressources associées à chaque utilisateur.

## 📝 Schémas Pydantic

Définis dans `sql_app/schemas.py`, ces schémas servent à valider les données entrantes et sortantes :

- **UserBase, UserCreate, User**: Pour les utilisateurs.
- **RessourceBase, RessourceCreate, Ressource**: Pour les ressources.

## 🗂 Opérations CRUD

Implémentées dans `sql_app/crud.py`, ces opérations facilitent la gestion des données :

- **Create, Read, Update, Delete**: Actions fondamentales pour les utilisateurs et leurs ressources.

## 🚦 Routes de l'API

### Utilisateurs

- **Créer un utilisateur** : `POST /users/`
- **Lire tous les utilisateurs** : `GET /users/`
- **Lire un utilisateur par ID** : `GET /users/{user_id}`

### Ressources

- **Créer une ressource pour un utilisateur** : `POST /users/{user_id}/ressources`

## 🏁 Démarrage de l'API


Pour démarrer l'API, utilisez la commande suivante :

```bash
uvicorn sql_app.main:app --reload --port 5000
```

Votre API est maintenant en cours d'exécution et accessible à [http://localhost:5000](http://localhost:5000) 🎉.

