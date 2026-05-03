from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Facture
from .forms import FactureForm


class FactureListView(ListView):
    """Affiche la liste de toutes les factures"""
    model = Facture
    template_name = 'factures/facture_list.html'
    context_object_name = 'factures'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Facture.objects.all()
        statut = self.request.GET.get('statut')
        if statut:
            queryset = queryset.filter(statut=statut)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuts'] = Facture.STATUS_CHOICES
        return context


class FactureDetailView(DetailView):
    """Affiche les détails d'une facture"""
    model = Facture
    template_name = 'factures/facture_detail.html'
    context_object_name = 'facture'
    pk_url_kwarg = 'pk'


class FactureCreateView(CreateView):
    """Crée une nouvelle facture"""
    model = Facture
    form_class = FactureForm
    template_name = 'factures/facture_form.html'
    success_url = reverse_lazy('facture_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Facture créée avec succès!')
        return super().form_valid(form)


class FactureUpdateView(UpdateView):
    """Modifie une facture existante"""
    model = Facture
    form_class = FactureForm
    template_name = 'factures/facture_form.html'
    success_url = reverse_lazy('facture_list')
    pk_url_kwarg = 'pk'
    
    def form_valid(self, form):
        messages.success(self.request, 'Facture mise à jour avec succès!')
        return super().form_valid(form)


class FactureDeleteView(DeleteView):
    """Supprime une facture"""
    model = Facture
    template_name = 'factures/facture_confirm_delete.html'
    success_url = reverse_lazy('facture_list')
    pk_url_kwarg = 'pk'
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Facture supprimée avec succès!')
        return super().delete(request, *args, **kwargs)
