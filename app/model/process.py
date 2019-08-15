from django.db import models

from app.model.negotiation import Negotiation


STATUS = (
    (0, 'inprocess'),
    (1, 'yescontract'),
    (2, 'cancelled')
)


class Process(models.Model):
    negotiation = models.ForeignKey(Negotiation, on_delete=models.CASCADE)
    cause = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)
    destination_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS)

    class Meta:
        db_table = 'processes'
        ordering = ['id']

    def __str__(self):
        return self.description

