from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.db import models
from django.contrib.auth.models import User 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    position = models.ForeignKey('Position', null=True, blank=True, on_delete=models.SET_NULL, related_name='profiles', verbose_name='Cargo')
    sector = models.ManyToManyField('Sector', blank=True, related_name='profiles', verbose_name='Setores')
    history = AuditlogHistoryField()

    def __str__(self):
        return f"{self.user.username}'s Profile"