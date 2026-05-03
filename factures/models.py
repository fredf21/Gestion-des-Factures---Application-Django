from django.db import models
from django.core.validators import MinValueValidator

class Facture(models.Model):
    STATUS_CHOICES = [
        ('brouillon', 'Brouillon'),
        ('envoyee', 'Envoyée'),
        ('payee', 'Payée'),
        ('annulee', 'Annulée'),
    ]
    
    numero = models.CharField(max_length=50, unique=True, verbose_name="Numéro de facture")
    client = models.CharField(max_length=100, verbose_name="Client")
    email_client = models.EmailField(blank=True, verbose_name="Email du client")
    date_facture = models.DateField(auto_now_add=True, verbose_name="Date de facture")
    date_echeance = models.DateField(verbose_name="Date d'échéance")
    description = models.TextField(verbose_name="Description/Articles")
    montant_total = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0)],
        verbose_name="Montant total"
    )
    statut = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='brouillon',
        verbose_name="Statut"
    )
    notes = models.TextField(blank=True, verbose_name="Notes")
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_facture']
        verbose_name = "Facture"
        verbose_name_plural = "Factures"
    
    def __str__(self):
        return f"Facture {self.numero} - {self.client} ({self.montant_total}€)"
