# Démarrage Rapide - Gestion des Factures

## Installation Express (2 minutes)

### Windows
```cmd
# 1. Accéder au répertoire du projet
cd c:\Users\fredf\CCNB_DEUXIEME_ANNEE\PROG-1373\INDIVIDUEL\projet3

# 2. Activer l'environnement virtuel (s'il n'existe pas)
python -m venv .venv
.venv\Scripts\activate

# 3. Installer Django
pip install -r requirements.txt

# 4. Appliquer les migrations
python manage.py migrate

# 5. (Optionnel) Charger les données de test
python setup_test_data.py

# 6. Lancer le serveur
python manage.py runserver
```

### macOS / Linux
```bash
# 1. Accéder au répertoire du projet
cd projet3

# 2. Activer l'environnement virtuel (s'il n'existe pas)
python3 -m venv .venv
source .venv/bin/activate

# 3. Installer Django
pip install -r requirements.txt

# 4. Appliquer les migrations
python manage.py migrate

# 5. (Optionnel) Charger les données de test
python setup_test_data.py

# 6. Lancer le serveur
python manage.py runserver
```

## 🌐 Accès à l'Application

- **Application** : http://localhost:8000/factures/
- **Admin Django** : http://localhost:8000/admin/
- **ID admin (par défaut)** : `admin`
- **Password (par défaut)** : `admin`

## Données de Test

Si vous avez exécuté `setup_test_data.py`, 5 factures de test sont disponibles:
- FAC-2024-001 (Payée) - Entreprise ABC SARL
- FAC-2024-002 (Envoyée) - Consultant Digital XYZ
- FAC-2024-003 (Brouillon) - Startup Tech Innovation
- FAC-2024-004 (Annulée) - Agence Marketing Plus
- FAC-2024-005 (Payée) - Formation Institute Pro

## 🎯 Premières Actions

### 1. Consulter les factures
```
1. Allez sur http://localhost:8000/factures/
2. Vous verrez la liste complète de toutes les factures
```

### 2. Créer une facture
```
1. Cliquez sur "Nouvelle Facture"
2. Remplissez le formulaire
3. Cliquez sur "Créer"
```

### 3. Modifier une facture
```
1. Cliquez sur l'icône "Modifier" (crayon)
2. Modifiez les informations
3. Cliquez sur "Mettre à jour"
```

### 4. Supprimer une facture
```
1. Cliquez sur l'icône "Supprimer" (poubelle)
2. Confirmez la suppression
```

### 5. Filtrer par statut
```
1. Utilisez le menu déroulant "Statuts"
2. Sélectionnez un statut (Brouillon, Envoyée, Payée, Annulée)
```

## Créer un Nouvel Administrateur

```bash
python manage.py createsuperuser
```

Suivez les prompts pour créer un nouvel administrateur.

## Troubleshooting

### Erreur de port (8000 déjà utilisé)
```bash
python manage.py runserver 8001
```
Puis accédez à http://localhost:8001/factures/

### Les migrations ne s'appliquent pas
```bash
python manage.py migrate --run-syncdb
```

### Réinitialiser la base de données
```bash
# Supprimer le fichier db.sqlite3
# Puis réappliquer les migrations
python manage.py migrate
```

## Configuration Avancée

### Changer le SECRET_KEY
Modifiez `facturesproject/settings.py` - ligne 23

### Modifier la base de données (PostgreSQL, MySQL...)
Modifiez `facturesproject/settings.py` - ligne DATABASES

### Ajouter des champs au modèle
1. Modifiez `factures/models.py`
2. Exécutez:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Support

Pour plus d'informations, consultez le README.md complet.
