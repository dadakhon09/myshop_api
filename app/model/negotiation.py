from django.db import models

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

    class Meta:
        db_table = 'negotiations'
        ordering = ['id']

    def __str__(self):
        return self.description

    def get_end_date(self):
        if self.process_set.filter(status='yescontract').count() > 0:
            return self.process_set.get(status='yescontract').created
        elif self.process_set.get(status='cancelled'):
            return self.process_set.get(status='cancelled').created
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

