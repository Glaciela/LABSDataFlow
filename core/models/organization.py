from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.db import models


class Organization(models.Model):
    """
    Modelo que representa uma Secretaria ou Autarquia da prefeitura municipal de Campo Grande.
    Cada departamento pode ter um nome e uma descrição.
    """
    organization_name = models.CharField(max_length=255, unique=True, null=False, blank=False, verbose_name='Nome da Secretaria ou Autarquia')
    organization_acronym = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name='Sigla da Secretaria ou Autarquia')
    organization_code = models.TextField(blank=False, null=False, unique=True, verbose_name='Código da Secretaria ou Autarquia')

    # Campo para armazenar o histórico de alterações
    history = AuditlogHistoryField()

    class Meta:
        verbose_name = 'Secretaria ou Autarquia'
        verbose_name_plural = 'Secretarias e Autarquias'

    def __str__(self):
        return self.organization_name
    
# Registrar o modelo para auditoria
auditlog.register(Organization)