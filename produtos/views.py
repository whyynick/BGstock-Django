from django.views.generic import ListView
# pyrefly: ignore [missing-import]
from produtos.models import Produto
# Create your views here.

class ProdutoListView(ListView):
    model = Produto
    template_name = "produtos/produto-lista.html"
    context_object_name = "Produtos"
    paginate_by = 10
