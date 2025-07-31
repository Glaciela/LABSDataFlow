from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.db import models


class Position(models.Model):
    """
    Modelo que representa um cargo dentro do sistema.
    Cada cargo pode ter um nome
    """
    position_name = models.CharField(max_length=150, null=False, blank=False, verbose_name='Nome do Cargo')
    type_position = models.ForeignKey('TypePosition', null=False, blank=False, on_delete=models.CASCADE, related_name='positions', verbose_name='Tipo de Cargo')
    
    # Campo para armazenar o histórico de alterações
    history = AuditlogHistoryField()

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.position_name

# Registrar o modelo para auditoria
auditlog.register(Position)