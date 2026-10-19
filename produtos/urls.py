from produtos.views import ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView
from django.urls import path

app_name = "produtos"

urlpatterns = [
    path("produtos/", ProdutoListView.as_view(), name="produtos_list"),
    path("produtos/create", ProdutoCreateView.as_view(), name="produtos_create"),
    path("produtos/<int:pk>/delete", ProdutoDeleteView.as_view(), name="produtos_delete"),
    path("produtos/<int:pk>/edit",ProdutoUpdateView.as_view(), name="produtos_update")
]