from django.db import models


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)

    def __str__(self):
        return self.motivo

    class Meta:
        verbose_name = 'RegistroHoraExtra'
        verbose_name_plural = 'RegistrosHoraExtra'
