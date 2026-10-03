from re import search
from django.contrib import admin
from produtos.models import Produto, Estoque
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("produto_nome","produto_genero")
    search_fields = ("produto_nome","produto_genero")

class EstoqueAdmin(admin.ModelAdmin):
    list_display = ("local","prateleira", "nivel_prateleira")
    search_fields = ("local","prateleira", "nivelprateleira")
    list_filter = ("local","prateleira")

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Estoque, EstoqueAdmin)
