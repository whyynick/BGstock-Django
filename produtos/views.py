from produtos.apps import ProdutosConfig
from produtos.form import ProdutoForm
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import Produto
# Create your views here.

class ProdutoListView(ListView):
    model = Produto
    template_name = "produtos/produtos_list.html"
    context_object_name = "produtos"
    paginate_by = 10

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produtos/produtos_create.html"
    success_url = reverse_lazy("produtos:produtos_list")
    login_url = reverse_lazy("admin:login")

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = "produtos/produtos_delete.html"
    context_object_name = "produtos"
    success_url = reverse_lazy("produtos:produtos_list")
    login_url = reverse_lazy("admin:login")

class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produtos/produtos_update.html"
    context_object_name = "produtos"
    success_url = reverse_lazy("produtos:produtos_list")
    login_url = reverse_lazy("admin:login")