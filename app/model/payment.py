from _decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from app.model.contract import Contract


class Payment(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    cash = models.DecimalField(decimal_places=0, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))],
                               null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    pay_day = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'payments'
        ordering = ['created']

    def __str__(self):
        return self.contract.description
