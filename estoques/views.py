from django.views.generic import ListView
from django.shortcuts import render
from estoques.models import Estoque
# Create your views here.

class EstoqueListView(ListView):
    model = Estoque
    template_name = "estoques/estoques.html"
    context_object_name = "Estoques"
    paginate_by = 10