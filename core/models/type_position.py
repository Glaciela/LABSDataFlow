from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.db import models


class TypePosition(models.Model):
    """
    Modelo que representa um tipo de cargo dentro do sistema.
    Cada tipo de cargo pode ter um nome e uma descrição.
    """
    type_name = models.CharField(max_length=150, null=False, blank=False, verbose_name='Nome do Tipo de Cargo')

    # Campo para armazenar o histórico de alterações
    history = AuditlogHistoryField()

    class Meta:
        verbose_name = 'Tipo de Cargo'
        verbose_name_plural = 'Tipos de Cargos'

    def __str__(self):
        return self.type_name
    
# Registrar o modelo para auditoria
auditlog.register(TypePosition)