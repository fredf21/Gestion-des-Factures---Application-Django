# Gestion des Factures - Application Django

Une application Web CRUD (Create, Read, Update, Delete) pour gérer une collection de factures, développée avec Django et Bootstrap.

## Description

Cette application permet de :
- **Créer** des factures avec numéro unique, client, dates et montants
- **Consulter** la liste complète des factures avec filtrage par statut
- **Afficher** les détails détaillés d'une facture
- **Modifier** les informations d'une facture existante
- **Supprimer** une facture avec confirmation
- **Filtrer** les factures par statut (Brouillon, Envoyée, Payée, Annulée)
- **Chercher** des factures par numéro ou nom de client

## Caractéristiques

### Architecture MVT (Modèle-Vue-Template)
- **Modèle** : Modèle `Facture` avec tous les champs nécessaires
- **Vues** : Utilisation de vues basées sur les classes (Class-Based Views) pour chaque opération CRUD
- **Templates** : Templates HTML élégants utilisant Bootstrap 5

### Fonctionnalités CRUD
- **Create** : Formulaire pour créer une nouvelle facture
- **Read** : Affichage des listes et des détails
- **Update** : Modification des factures existantes
- **Delete** : Suppression avec confirmation

### Design et UX
- Interface moderne avec Bootstrap 5
- Navigation intuitive
- Responsive design (mobile-friendly)
- Icônes avec Font Awesome
- Palette de couleurs cohérente
- Messages de feedback utilisateur

### Gestion des Factures
- Numéro de facture unique
- Informations client (nom, email)
- Dates de facturation et d'échéance
- Description détaillée des articles/services
- Montant total validé
- Statut de facturation
- Notes supplémentaires
- Suivi des dates de création et modification

## Structure du Projet

```
projet3/
├── .venv/                          # Environnement virtuel Python
├── facturesproject/                 # Configuration du projet Django
│   ├── settings.py                 # Paramètres Django
│   ├── urls.py                     # Routage principal
│   ├── wsgi.py                     # Configuration WSGI
│   └── manage.py                   # Utilitaire de gestion Django
├── factures/                        # Application Django
│   ├── migrations/                 # Migrations de base de données
│   ├── templates/
│   │   └── factures/
│   │       ├── base.html           # Template de base
│   │       ├── facture_list.html   # Listing des factures
│   │       ├── facture_detail.html # Détail d'une facture
│   │       ├── facture_form.html   # Formulaire créer/modifier
│   │       └── facture_confirm_delete.html  # Confirmation suppression
│   ├── models.py                   # Modèle Facture
│   ├── views.py                    # Vues CRUD
│   ├── forms.py                    # Formulaires Django
│   ├── urls.py                     # Routage de l'app
│   ├── admin.py                    # Configuration interface admin
│   └── apps.py                     # Configuration de l'application
├── db.sqlite3                       # Base de données (créée après migration)
└── README.md                        # Ce fichier
```

## Installation et Configuration

### Prérequis
- Python 3.8+
- pip

### Étapes d'installation

1. **Cloner le projet** (ou extraire les fichiers)
   ```bash
   cd projet3
   ```

2. **Créer et activer l'environnement virtuel**
   ```bash
   # Sur Windows
   .venv\Scripts\activate
   
   # Sur macOS/Linux
   source .venv/bin/activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install django
   ```

4. **Appliquer les migrations**
   ```bash
   python manage.py migrate
   ```

5. **Créer un superutilisateur (administrateur)**
   ```bash
   python manage.py createsuperuser
   ```
   Suivez les prompts pour créer votre compte administrateur.

6. **Lancer le serveur de développement**
   ```bash
   python manage.py runserver
   ```

7. **Accéder à l'application**
   - Ouvrir le navigateur à: `http://localhost:8000/factures/`
   - Admin Django: `http://localhost:8000/admin/`

## 📖 Utilisation

### Page d'Accueil
Affiche la liste complète de toutes les factures avec:
- Numéro de facture
- Nom du client
- Date de facturation
- Montant total
- Statut (avec couleur code)
- Actions (Voir, Modifier, Supprimer)

### Créer une Facture
1. Cliquez sur "Nouvelle Facture"
2. Remplissez le formulaire:
   - Numéro de facture (unique)
   - Nom du client
   - Email du client (optionnel)
   - Date d'échéance
   - Description des articles/services
   - Montant total
   - Statut initial
   - Notes (optionnel)
3. Cliquez sur "Créer"

### Afficher les Détails
1. Cliquez sur l'icône "Voir" dans la liste
2. Consultez tous les détails de la facture
3. Utilisez les boutons pour modifier ou supprimer

### Modifier une Facture
1. Cliquez sur l'icône "Modifier"
2. Modifiez les champs souhaités
3. Cliquez sur "Mettre à jour"

### Supprimer une Facture
1. Cliquez sur l'icône "Supprimer"
2. Confirmez la suppression (action irréversible)

### Filtrer et Chercher
- **Filtrer par statut** : Utilisez le menu déroulant "Statuts"
- **Rechercher** : Utilisez le champ de recherche pour filtrer par numéro ou client

## Base de Données

### Modèle Facture
```python
class Facture(models.Model):
    numero = CharField (unique)           # Numéro de facture
    client = CharField                    # Nom du client
    email_client = EmailField            # Email (optionnel)
    date_facture = DateField             # Date auto (jour de création)
    date_echeance = DateField            # Date d'échéance
    description = TextField              # Articles/services
    montant_total = DecimalField         # Montant (2 décimales)
    statut = CharField                   # Brouillon, Envoyée, Payée, Annulée
    notes = TextField                    # Notes supplémentaires
    date_creation = DateTimeField        # Timestamp création
    date_modification = DateTimeField    # Timestamp modification
```

### Statuts disponibles
- 🟡 **Brouillon** : Facture en cours de rédaction
- 🔵 **Envoyée** : Facture envoyée au client
- 🟢 **Payée** : Facture payée
- 🔴 **Annulée** : Facture annulée

## Gestion des Erreurs

L'application gère les erreurs courantes:
- Validation des montants (positifs uniquement)
- Validation des emails
- Unicité des numéros de facture
- Messages d'erreur détaillés
- Confirmation avant suppression

## Personnalisation

### Modifier les couleurs
Éditer le fichier `factures/templates/factures/base.html` et modifier les variables CSS:
```css
:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --success-color: #27ae60;
    --danger-color: #e74c3c;
    --warning-color: #f39c12;
}
```

### Ajouter des champs
1. Modifier le modèle dans `factures/models.py`
2. Créer et appliquer une migration:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Ajouter les champs dans `factures/forms.py`
4. Mettre à jour les templates

## Interface d'Administration

Accédez à l'interface admin sur `http://localhost:8000/admin/`:
- Authentifiez-vous avec votre compte superutilisateur
- Gérez les factures directement
- Filtrez par statut et date
- Recherchez par numéro ou client
- Modifiez le statut en ligne

## Critères d'Évaluation Répondus

### Architecture MVT (10 pts)
- Modèles : Modèle `Facture` bien structuré
- Vues : Class-Based Views pour chaque opération
- Templates : Templates réutilisables avec `base.html`

### Fonctionnalités CRUD (8 pts)
- **Create** : Formulaire de création fonctionnel
- **Read** : Listing et détails affichés correctement
- **Update** : Modification des factures possible
- **Delete** : Suppression avec confirmation

### Routage et Navigation (6 pts)
- URLs logiques et cohérentes
- Navigation fluide entre pages
- Breadcrumbs et liens contextuels
- Redirection appropriée après actions

### Présentation CSS (6 pts)
- Bootstrap 5 intégré
- Design moderne et responsive
- Iconographie avec Font Awesome
- Cohérence visuelle et UX

## Dépannage

### Le serveur ne démarre pas
```bash
# Vérifiez que le port 8000 est libre
python manage.py runserver 8001
```

### Erreur de base de données
```bash
# Supprimez et recréez la BD
rm db.sqlite3
python manage.py migrate
```

### Les templates ne s'affichent pas
Assurez-vous que 'APP_DIRS' est `True` dans `settings.py` TEMPLATES.

## Ressources

- [Documentation Django 6.0](https://docs.djangoproject.com/en/6.0/)
- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.0/)
- [Font Awesome Icons](https://fontawesome.com/icons)

## Auteur

Projet réalisé par Ky Frederic
