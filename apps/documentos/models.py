from django.db import models
from ..funcionarios.models import Funcionario

class Documento(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

