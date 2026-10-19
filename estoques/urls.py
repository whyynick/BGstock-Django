from estoques.views import EstoqueListView, EstoqueCreateView, EstoqueDeleteView, EstoqueUpdateView
from django.urls import path, include

app_name = "estoques"

urlpatterns = [
   path("estoques/", EstoqueListView.as_view(), name="estoques_list"),
   path("estoques/create", EstoqueCreateView.as_view(), name="estoque_create"),
   path("estoques/<int:pk>/delete",EstoqueDeleteView.as_view(), name="estoque_delete"),
   path("estoques/<int:pk>/update", EstoqueUpdateView.as_view(), name= "estoque_update"),
]