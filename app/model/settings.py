from _decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from app.model import Negotiation


class Settings(models.Model):
    negotiation_durability = models.DecimalField(decimal_places=0, max_digits=12,
                                                 validators=[MinValueValidator(Decimal('0.01'))], default=2, null=True,
                                                 blank=True, unique=True)
    # negotiation = models.ForeignKey(Negotiation, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'settings'

    def __str__(self):
        return str(self.negotiation_durability)
