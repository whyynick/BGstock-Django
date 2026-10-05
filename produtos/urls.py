from django.urls import path
from produtos.views import ProdutoListView

app_name = "produtos"

urlpatterns = [
    path("produtos/", ProdutoListView.as_view(), name="person_list")
]