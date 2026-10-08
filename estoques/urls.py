from estoques.views import EstoqueUpdateView
from estoques.views import EstoqueListView
from django.urls import path, include

app_name = "estoques"

urlpatterns = [
   path("estoques/", EstoqueListView.as_view(), name="estoque_list"),
   path("estoques/<int:pk>/editar/", EstoqueUpdateView.as_view(), name= "estoque_update"),
]