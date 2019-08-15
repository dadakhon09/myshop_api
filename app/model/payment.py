from django.db import models

from app.model.contract import Contract


class Payment(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    cash = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)
    pay_day = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'payments'
        ordering = ['created']

    def __str__(self):
        return self.created

