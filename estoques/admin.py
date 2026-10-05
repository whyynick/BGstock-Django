from django.contrib import admin
from estoques.models import Estoque
# Register your models here.

class EstoqueAdmin(admin.ModelAdmin):
    list_display = ("produto","local","prateleira", "nivel_prateleira")
    search_fields = ("local","prateleira")
    list_filter = ("local","prateleira")

admin.site.register(Estoque, EstoqueAdmin)
