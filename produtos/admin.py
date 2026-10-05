from re import search
from django.contrib import admin
from produtos.models import Produto
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("produto_nome","produto_genero")
    search_fields = ("produto_nome","produto_genero")
    
admin.site.register(Produto, ProdutoAdmin)