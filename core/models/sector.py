from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.db import models


class Sector(models.Model):
    """
    Modelo que representa um setor da prefeitura municipal de campo grande
    dentro do sistema.
    Cada setor pode ter um nome e uma descrição.
    """
    sector_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Nome do Setor')
    sector_acronym = models.CharField(max_length=50, verbose_name='Sigla do Setor')
    sector_code = models.TextField(null=False, blank=False, unique=True, verbose_name='Código do Setor')
    organization = models.ForeignKey('Organization', null=False, blank=False, on_delete=models.CASCADE, related_name='sectors', verbose_name='Secretaria ou Autarquia')
    
    # Campo para armazenar o histórico de alterações
    history = AuditlogHistoryField()

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'

    def __str__(self):
        return self.name

# Registrar o modelo para auditoria
auditlog.register(Sector)