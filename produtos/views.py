from produtos.form import ProdutoForm
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from .models import Produto
# Create your views here.

class ProdutoListView(ListView):
    model = Produto
    template_name = "produtos/produtos_list.html"
    context_object_name = "produtos"
    paginate_by = 10

class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produtos/produtos_form.html"
    context_object_name = "produto"
    success_url = reverse_lazy("produtos:produtos_list")
    login_url = reverse_lazy("admin:login")