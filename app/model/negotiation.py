import datetime

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from app.model import Action
from app.model.partner import Partner


STATUS = (
    (0, 'inprocess'),
    (1, 'yescontract'),
    (2, 'cancelled')
)


class Negotiation(models.Model):
    created = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255, blank=True)
    contract = models.OneToOneField('Contract', on_delete=models.CASCADE, blank=True, null=True)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, blank=True, null=True)
    actions = GenericRelation(Action)

    @property
    def sphere(self):
        return 'Negotiation'
    
    class Meta:
        db_table = 'negotiations'
        ordering = ['id']

    def __str__(self):
        return self.description

    def get_end_date(self):
        if self.process_set.filter(status=0).count() > 0:
            return self.process_set.filter(status=0).created
        elif self.process_set.filter(status=2):
            return self.process_set.filter(status=2).created
        else:
            return 'Идёт переговоры'

    def meets(self):
        today = datetime.date.today()
        if self.status == 'yescontract':
            return self.process_set.filter(status='no', destination_date__year=today.year,
                                           destination_date__month=today.month, destination_date__day=today.day)
        else:
            return self.process_set.filter(status='inprocess', destination_date__year=today.year,
                                           destination_date__month=today.month, destination_date__day=today.day)

