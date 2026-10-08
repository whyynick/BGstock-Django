from produtos.views import ProdutoUpdateView
from django.urls import path
from produtos.views import ProdutoListView

app_name = "produtos"

urlpatterns = [
    path("produtos/", ProdutoListView.as_view(), name="produtos_list"),
    path("produtos/<int:pk>/editar",ProdutoUpdateView.as_view(), name="produtos_update"),
]