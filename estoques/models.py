from django.db import models
from produtos.models import Produto
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Estoque(models.Model):
    CORREDOR_CHOICES = [
        ("0", "Área de Manuseio"),
        ("A", "Primeiro Corredor"),
        ("B", "Segundo Corredor"),
        ("C", "Terceiro Corredor"),
    ]

    produto = models.ForeignKey(
        Produto,
        on_delete = models.CASCADE,
        verbose_name = "Produto"
    )

    local = models.CharField(
        verbose_name = "Corredor",
        max_length = 1,
        choices = CORREDOR_CHOICES,
        default = "0",
    )
   

    prateleira = models.IntegerField(verbose_name="Prateleira",validators=[MinValueValidator(1),MaxValueValidator(5)])
    nivel_prateleira = models.IntegerField(verbose_name="Nível prateleira", validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        verbose_name = "Estoque"
        verbose_name_plural = "Estoques"
        ordering = ["prateleira"]

    def __str__(self):
        return f"Prateleira{self.prateleira} - {self.local}"
    
