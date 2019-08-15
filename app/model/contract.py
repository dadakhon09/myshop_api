from django.db import models


class Contract(models.Model):
    price = models.CharField(max_length=255)
    signing_date = models.DateField(null=True, blank=True)
    activation_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    duration = models.CharField(max_length=255)
    tariff = models.ForeignKey("Tariff", on_delete=models.SET_NULL, null=True, blank=True)
    tariff_price = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

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

