from _pydecimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from app.model.contract import Contract


class MediaPlan(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True, blank=True)
    current_month = models.DecimalField(decimal_places=0, max_digits=2,
                                        validators=[MinValueValidator(Decimal('0.01'))], null=True, blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    @property
    def sphere(self):
        return 'MediaPlan'
    
    class Meta:
        db_table = 'mediaplans'
        ordering = ['id']

    def __str__(self):
        return self.description


class Document(models.Model):
    document = models.FileField(upload_to='', blank=True, null=True)
    mediaplan = models.ForeignKey('MediaPlan', on_delete=models.CASCADE, related_name='documents')

    class Meta:
        db_table = 'documents'
        ordering = ['-id']

    def __str__(self):
        return self.document.name
