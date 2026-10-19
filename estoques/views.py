from django.db.models.fields import reverse_related
from estoques.forms import EstoqueForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.shortcuts import render
from estoques.models import Estoque
# Create your views here.

class EstoqueListView(ListView):
    model = Estoque
    template_name = "estoques/estoques_list.html"
    context_object_name = "Estoques"
    paginate_by = 10

class EstoqueCreateView(CreateView):
    model = Estoque
    form_class = EstoqueForm
    template_name = "estoques/estoques_create.html"
    success_url = reverse_lazy("estoques:estoques_list")
    login_url = reverse_lazy("admin:login")

class EstoqueDeleteView(DeleteView):
    model = Estoque
    template_name = "estoques/estoques_delete.html"
    context_object_name = "Estoque"
    success_url = reverse_lazy("estoques:estoques_list")
    login_url = reverse_lazy("admin:login")

class EstoqueUpdateView(LoginRequiredMixin, UpdateView):
    model = Estoque
    form_class = EstoqueForm
    template_name = "estoques/estoques_update.html"
    context_object_name = "Estoque"
    success_url = reverse_lazy("estoques:estoques_list")
    login_url = reverse_lazy("admin:login")