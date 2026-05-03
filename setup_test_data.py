#!/usr/bin/env python
"""
Script d'initialisation avec données de test
À exécuter après les migrations: python setup_test_data.py
"""

import os
import sys
import django
from datetime import datetime, timedelta

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'facturesproject.settings')
django.setup()

from django.contrib.auth.models import User
from factures.models import Facture

def create_superuser():
    """Crée un superutilisateur pour l'admin"""
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
        print("✅ Superutilisateur créé: admin / admin")
    else:
        print("ℹ️  Superutilisateur 'admin' existe déjà")

def create_sample_factures():
    """Crée des factures de test"""
    if Facture.objects.exists():
        print("✅ Données de test existent déjà")
        return
    
    factures_data = [
        {
            'numero': 'FAC-2024-001',
            'client': 'Entreprise ABC SARL',
            'email_client': 'contact@abc.fr',
            'date_echeance': datetime.now().date() + timedelta(days=30),
            'description': '- Développement application web\n- Support technique (10h)\n- Maintenance serveur',
            'montant_total': 2500.00,
            'statut': 'payee',
            'notes': 'Client régulier - Facture payée le 15/04/2024'
        },
        {
            'numero': 'FAC-2024-002',
            'client': 'Consultant Digital XYZ',
            'email_client': 'info@xyz.fr',
            'date_echeance': datetime.now().date() + timedelta(days=15),
            'description': '- Consulting stratégie digitale (20h)\n- Rapport d\'analyse concurrentielle\n- Recommandations SEO',
            'montant_total': 1800.00,
            'statut': 'envoyee',
            'notes': 'En attente de paiement'
        },
        {
            'numero': 'FAC-2024-003',
            'client': 'Startup Tech Innovation',
            'email_client': 'billing@startup.io',
            'date_echeance': datetime.now().date() + timedelta(days=60),
            'description': '- License logiciel annuelle\n- Support premium inclus\n- Mise à jour automatique',
            'montant_total': 5000.00,
            'statut': 'brouillon',
            'notes': 'Facture en attente de validation - Contrat en cours de négociation'
        },
        {
            'numero': 'FAC-2024-004',
            'client': 'Agence Marketing Plus',
            'email_client': 'facturation@agenceplus.fr',
            'date_echeance': datetime.now().date() - timedelta(days=10),
            'description': '- Campagne publicitaire Google Ads\n- Gestion des réseaux sociaux (3 mois)\n- Reporting mensuel',
            'montant_total': 3600.00,
            'statut': 'annulee',
            'notes': 'Contrat annulé - Facture annulée le 05/04/2024'
        },
        {
            'numero': 'FAC-2024-005',
            'client': 'Formation Institute Pro',
            'email_client': 'comptabilite@formation.edu',
            'date_echeance': datetime.now().date() + timedelta(days=45),
            'description': '- Formation Python (40h)\n- Matériel pédagogique\n- Certification incluse\n- Support post-formation (3 mois)',
            'montant_total': 4200.00,
            'statut': 'payee',
            'notes': 'Formation complétée - Tous les participants certifiés'
        },
    ]
    
    for data in factures_data:
        facture = Facture(**data)
        facture.save()
        print(f"✅ Facture créée: {facture.numero} - {facture.client}")

def main():
    print("🚀 Initialisation de l'application avec données de test...\n")
    create_superuser()
    create_sample_factures()
    print("\n✅ Initialisation complète!")
    print("📌 Accédez à l'admin: http://localhost:8000/admin/")
    print("   Identifiant: admin")
    print("   Mot de passe: admin")
    print("📌 Accédez à l'app: http://localhost:8000/factures/")

if __name__ == '__main__':
    main()
