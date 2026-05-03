# 📍 Points d'Entrée - Architecture MVT

## Vue d'ensemble de l'Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    URLS (Routage)                            │
├─────────────────────────────────────────────────────────────┤
│  facturesproject/urls.py ──> factures/urls.py               │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│               VIEWS (Logique métier)                        │
├─────────────────────────────────────────────────────────────┤
│  FactureListView    (GET liste)                             │
│  FactureDetailView  (GET détails)                           │
│  FactureCreateView  (GET form + POST create)                │
│  FactureUpdateView  (GET form + POST update)                │
│  FactureDeleteView  (GET form + POST delete)                │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│              MODELS (Base de données)                       │
├─────────────────────────────────────────────────────────────┤
│  Facture                                                     │
│  ├── numero (CharField, unique)                            │
│  ├── client (CharField)                                    │
│  ├── email_client (EmailField)                             │
│  ├── date_facture (DateField, auto)                        │
│  ├── date_echeance (DateField)                             │
│  ├── description (TextField)                              │
│  ├── montant_total (DecimalField)                         │
│  ├── statut (CharField, choices)                          │
│  ├── notes (TextField)                                    │
│  ├── date_creation (DateTimeField, auto)                  │
│  └── date_modification (DateTimeField, auto)              │
└─────────────────────────────────────────────────────────────┘
```

## Flux Requête-Réponse

### 1️ Lister les factures
```
GET /factures/
  ├─> facturesproject/urls.py (path('factures/', include('factures.urls')))
  ├─> factures/urls.py (path('', FactureListView.as_view(), name='facture_list'))
  ├─> factures/views.py (FactureListView.get_queryset(), get_context_data())
  ├─> factures/models.py (Facture.objects.all())
  ├─> DB Query (SELECT * FROM factures_facture)
  └─> factures/templates/factures/facture_list.html
```

### 2️ Voir les détails d'une facture
```
GET /factures/<id>/
  ├─> factures/urls.py (path('<int:pk>/', FactureDetailView.as_view(), name='facture_detail'))
  ├─> factures/views.py (FactureDetailView.get_object())
  ├─> factures/models.py (Facture.objects.get(pk=<id>))
  ├─> DB Query (SELECT * FROM factures_facture WHERE id = <id>)
  └─> factures/templates/factures/facture_detail.html
```

### 3️ Créer une facture
```
GET  /factures/create/
  ├─> factures/urls.py (path('create/', FactureCreateView.as_view(), name='facture_create'))
  ├─> factures/views.py (FactureCreateView.get_form())
  ├─> factures/forms.py (FactureForm())
  └─> factures/templates/factures/facture_form.html (formulaire vide)

POST /factures/create/
  ├─> factures/forms.py (FactureForm.is_valid())
  ├─> factures/models.py (Facture.save())
  ├─> DB Query (INSERT INTO factures_facture VALUES(...))
  └─> Redirection vers /factures/ + message de succès
```

### 4 Modifier une facture
```
GET  /factures/<id>/update/
  ├─> factures/urls.py (path('<int:pk>/update/', FactureUpdateView.as_view(), name='facture_update'))
  ├─> factures/views.py (FactureUpdateView.get_object(), get_form())
  ├─> factures/forms.py (FactureForm(instance=facture))
  └─> factures/templates/factures/facture_form.html (pré-rempli)

POST /factures/<id>/update/
  ├─> factures/forms.py (FactureForm.is_valid())
  ├─> factures/models.py (Facture.save())
  ├─> DB Query (UPDATE factures_facture SET ... WHERE id = <id>)
  └─> Redirection vers /factures/ + message de succès
```

### 5️ Supprimer une facture
```
GET  /factures/<id>/delete/
  ├─> factures/urls.py (path('<int:pk>/delete/', FactureDeleteView.as_view(), name='facture_delete'))
  ├─> factures/views.py (FactureDeleteView.get_object())
  └─> factures/templates/factures/facture_confirm_delete.html

POST /factures/<id>/delete/
  ├─> factures/models.py (Facture.delete())
  ├─> DB Query (DELETE FROM factures_facture WHERE id = <id>)
  └─> Redirection vers /factures/ + message de succès
```

## Fichiers Clés

### facturesproject/ (Projet Django)
| Fichier | Description |
|---------|-------------|
| `settings.py` | Configuration du projet (BD, apps, middleware, etc.) |
| `urls.py` | Routage principal du projet |
| `wsgi.py` | Configuration WSGI pour déploiement |

### factures/ (Application Django)
| Fichier | Description |
|---------|-------------|
| `models.py` | Définition du modèle Facture (BD) |
| `views.py` | Vues CRUD (logique métier) |
| `forms.py` | Formulaire pour Facture |
| `urls.py` | Routage spécifique à l'app |
| `admin.py` | Interface d'administration |
| `templates/` | Templates HTML |
| `migrations/` | Historique des changements de BD |

## 🎭 Vues (Class-Based Views)

Chaque vue hérite de Django Generic Views:

```python
# Héritage Django CBV
FactureListView(ListView)         # List + template
FactureDetailView(DetailView)     # Detail + template
FactureCreateView(CreateView)     # Form + POST handling
FactureUpdateView(UpdateView)     # Form + POST handling
FactureDeleteView(DeleteView)     # Confirmation + DELETE
```

### Cycle de vie d'une CreateView

```python
class FactureCreateView(CreateView):
    model = Facture           # Modèle à utiliser
    form_class = FactureForm  # Formulaire
    template_name = 'factures/facture_form.html'
    success_url = reverse_lazy('facture_list')
    
    # Quand on accède à /factures/create/ (GET)
    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)
    
    # Quand on soumet le formulaire (POST)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save()  # Sauvegarde en DB
            messages.success(request, 'Facture créée!')
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})
```

## Forms

```python
class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = [...]  # Champs du formulaire
        widgets = {     # Widgets Bootstrap
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            # ...
        }
```

## 📋 Templates

### Hiérarchie Template
```
base.html (Template de base avec Bootstrap)
├── facture_list.html (Listing)
├── facture_detail.html (Détails)
├── facture_form.html (Création/Modification)
└── facture_confirm_delete.html (Suppression)
```

### Variables dans templates
```html
<!-- facture_list.html -->
{% for facture in factures %}
  {{ facture.numero }}
  {{ facture.client }}
  {{ facture.get_statut_display }}
{% endfor %}
```

## Sécurité CSRF

Tout formulaire POST utilise le token CSRF:
```html
<form method="post">
    {% csrf_token %}
    {{ form }}
</form>
```

## 🎨 CSS Bootstrap

Intégré via CDN dans `base.html`:
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
```

## ⚙️ Configuration Importantes

### settings.py
```python
INSTALLED_APPS = [
    # ...
    'factures',  # Notre applicationm
]

TEMPLATES = [{
    'APP_DIRS': True,  # Cherche templates dans app/ 
}]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # SQLite locale
    }
}
```

### factures/urls.py
```python
urlpatterns = [
    path('', FactureListView.as_view(), name='facture_list'),
    path('<int:pk>/', FactureDetailView.as_view(), name='facture_detail'),
    path('create/', FactureCreateView.as_view(), name='facture_create'),
    path('<int:pk>/update/', FactureUpdateView.as_view(), name='facture_update'),
    path('<int:pk>/delete/', FactureDeleteView.as_view(), name='facture_delete'),
]
```

## Points de Déploiement

Pour déployer en production, modifiez:
1. `settings.py` DEBUG = False
2. `settings.py` ALLOWED_HOSTS
3. Utilisez une vraie base de données (PostgreSQL, MySQL)
4. Utilisez un serveur WSGI (Gunicorn, uWSGI)
5. Configurez un reverse proxy (Nginx, Apache)

---
**Comprendre cette architecture vous aide à:**
- Ajouter de nouvelles fonctionnalités
- Déboguer des problèmes
- Déployer l'application
- Collaborer avec d'autres développeurs
