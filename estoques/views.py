from django.db.models.fields import reverse_related
from estoques.forms import EstoqueForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from django.shortcuts import render
from estoques.models import Estoque
# Create your views here.

class EstoqueListView(ListView):
    model = Estoque
    template_name = "estoques/estoques_list.html"
    context_object_name = "Estoques"
    paginate_by = 10

class EstoqueUpdateView(LoginRequiredMixin, UpdateView):
    model = Estoque
    form_class = EstoqueForm
    template_name = "estoques/estoques_form.html"
    context_object_name = "estoque"
    success_url = reverse_lazy("estoques:estoque_list")
    login_url = reverse_lazy("admin:login")