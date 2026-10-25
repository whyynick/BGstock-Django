from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models.fields import reverse_related
from estoques.forms import EstoqueForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.shortcuts import render
from estoques.models import Estoque
# Create your views here.

class EstoqueListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Estoque
    template_name = "estoques/estoques_list.html"
    context_object_name = "Estoques"
    paginate_by = 10
    login_url = reverse_lazy("accounts:login")
    permission_required = ("estoques.view_estoque")

class EstoqueCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Estoque
    form_class = EstoqueForm
    template_name = "estoques/estoques_create.html"
    success_url = reverse_lazy("estoques:estoques_list")
    login_url = reverse_lazy("accounts:login")
    permission_required = ("estoques.add_estoque")

class EstoqueDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Estoque
    template_name = "estoques/estoques_delete.html"
    context_object_name = "Estoque"
    success_url = reverse_lazy("estoques:estoques_list")
    login_url = reverse_lazy("accounts:login")
    permission_required = ("estoques.delete_estoque")

class EstoqueUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Estoque
    form_class = EstoqueForm
    template_name = "estoques/estoques_update.html"
    context_object_name = "Estoque"
    success_url = reverse_lazy("estoques:estoques_list")
    login_url = reverse_lazy("accounts:login")
    permission_required = ("estoques.change_estoque")