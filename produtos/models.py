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
        verbose_name_plural = "Produtos"
        ordering = ["produto_nome"]
    
    def __str__(self):
        return f"{self.produto_nome} {self.produto_genero}"

class Estoque(models.Model):
    CORREDOR_CHOICES = [
        ("0", "Área de Manuseio"),
        ("A", "Primeiro Corredor"),
        ("B", "Segundo Corredor"),
        ("C", "Terceiro Corredor"),
    ]

    prateleira = models.IntegerField(verbose_name="Prateleira",validators=[MinValueValidator(1),MaxValueValidator(5)])
    nivel_prateleira = models.IntegerField(verbose_name="Prateleira", validators=[MinValueValidator(1), MaxValueValidator(5)])

    local = models.CharField(
        verbose_name = "Corredor",
        max_length = 1,
        choices = CORREDOR_CHOICES,
        default = "0",
    )
    produto = models.ForeignKey(
        Produto,
        on_delete = models.CASCADE,
        verbose_name = "Produto"
    )

    class Meta:
        verbose_name = "Estoque"
        verbose_name_plural = "Estoques"
        ordering = ["prateleira"]

    def __str__(self):
        return f"Prateleira{self.prateleira} - {self.local}"
    

