from _decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Contract(models.Model):
    price = models.DecimalField(decimal_places=0, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))],
                                null=True, blank=True)
    signing_date = models.DateField(null=True, blank=True)
    activation_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    duration = models.DecimalField(decimal_places=0, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))],
                                   null=True, blank=True)
    tariff = models.ForeignKey("Tariff", on_delete=models.SET_NULL, null=True, blank=True)
    tariff_price = models.DecimalField(decimal_places=0, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))],
                                       null=True, blank=True)
    description = models.CharField(max_length=255)

    @property
    def sphere(self):
        return 'Contract'
    
    class Meta:
        db_table = 'contracts'
        ordering = ['id']

    def __str__(self):
        return self.description

    def paid(self):
        paid_cash = 0
        for payment in self.payment_set.all().values('cash'):
            paid_cash += int(payment['cash'])
        return paid_cash

    def debt(self):

        return int(self.price) - self.paid()
