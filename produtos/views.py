from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from produtos.apps import ProdutosConfig
from produtos.form import ProdutoForm
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import Produto
# Create your views here.

class ProdutoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Produto
    template_name = "produtos/produtos_list.html"
    context_object_name = "produtos"
    paginate_by = 10
    login_url = reverse_lazy("accounts:login")
    permission_required = ("produtos.view_produto")

class ProdutoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produtos/produtos_create.html"
    success_url = reverse_lazy("produtos:produtos_list")
    login_url = reverse_lazy("accounts:login")
    permission_required = ("produtos.add_produto")

class ProdutoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Produto
    template_name = "produtos/produtos_delete.html"
    context_object_name = "produtos"
    success_url = reverse_lazy("produtos:produtos_list")
    login_url = reverse_lazy("accounts:login")
    permission_required = ("produtos.delete_produto")

class ProdutoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produtos/produtos_update.html"
    context_object_name = "produtos"
    success_url = reverse_lazy("produtos:produtos_list")
    login_url = reverse_lazy("accounts:login")
    permission_required = ("produtos.change_produto")