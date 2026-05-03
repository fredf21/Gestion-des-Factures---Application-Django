from django.urls import path
from . import views

urlpatterns = [
    # Accueil (redirection vers la liste)
    path('', views.FactureListView.as_view(), name='facture_list'),
    
    # Détail d'une facture
    path('<int:pk>/', views.FactureDetailView.as_view(), name='facture_detail'),
    
    # Création d'une facture
    path('create/', views.FactureCreateView.as_view(), name='facture_create'),
    
    # Modification d'une facture
    path('<int:pk>/update/', views.FactureUpdateView.as_view(), name='facture_update'),
    
    # Suppression d'une facture
    path('<int:pk>/delete/', views.FactureDeleteView.as_view(), name='facture_delete'),
]
