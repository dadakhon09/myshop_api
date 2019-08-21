from django.db import models
from django.contrib.auth.models import User

from app.model.negotiation import Negotiation


STATUS = (
    (0, 'inprocess'),
    (1, 'yescontract'),
    (2, 'cancelled')
)


class Process(models.Model):
    moder = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cause = models.CharField(max_length=255)
    negotiation = models.ForeignKey(Negotiation, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now=True)
    destination_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        db_table = 'processes'
        ordering = ['id']

    def __str__(self):
        return self.description or 'asd'

