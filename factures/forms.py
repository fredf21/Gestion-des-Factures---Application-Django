from django import forms
from .models import Facture


class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['numero', 'client', 'email_client', 'date_echeance', 'description', 'montant_total', 'statut', 'notes']
        widgets = {
            'numero': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: FAC-2024-001'
            }),
            'client': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom du client'
            }),
            'email_client': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email du client'
            }),
            'date_echeance': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Détail des articles ou services'
            }),
            'montant_total': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': '0.00'
            }),
            'statut': forms.Select(attrs={
                'class': 'form-control'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Notes supplémentaires'
            }),
        }
