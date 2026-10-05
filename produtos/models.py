from django.core import validators
from django.db.models.fields import reverse_related
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
# Create your models here.

class Produto(models.Model):
    produto_nome = models.CharField(verbose_name="Nome",max_length=30)
    produto_genero = models.CharField(verbose_name="Gênero", max_length=30)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Gerenciador de Produtos"
        ordering = ["produto_nome"]
    
    def __str__(self):
        return (f"Nome do item: {self.produto_nome} | Gênero do item: {self.produto_genero}")