from estoques.views import EstoqueListView
from django.urls import path, include

urlpatterns = [
   path("estoques/", EstoqueListView.as_view(), name="estoque_list")
]