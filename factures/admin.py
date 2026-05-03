from django.contrib import admin
from .models import Facture


@admin.register(Facture)
class FactureAdmin(admin.ModelAdmin):
    list_display = ['numero', 'client', 'montant_total', 'statut', 'date_facture']
    list_filter = ['statut', 'date_facture']
    search_fields = ['numero', 'client', 'email_client']
    list_editable = ['statut']
    date_hierarchy = 'date_facture'
    ordering = ['-date_facture']
    
    fieldsets = (
        ('Informations', {
            'fields': ('numero', 'client', 'email_client')
        }),
        ('Dates', {
            'fields': ('date_facture', 'date_echeance')
        }),
        ('Montant', {
            'fields': ('montant_total', 'description')
        }),
        ('Statut et Notes', {
            'fields': ('statut', 'notes')
        }),
    )
    
    readonly_fields = ('date_creation', 'date_modification', 'date_facture')
