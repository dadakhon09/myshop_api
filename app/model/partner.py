import datetime

from django.contrib.contenttypes.fields import GenericRelation
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.db import models

from app.model import Action


class Partner(models.Model):
    ooo = models.CharField(max_length=255, unique=True)
    contact_name = models.CharField(max_length=255, blank=True)
    stationary_phone = PhoneNumberField(blank=True, null=True)
    mobile_phone = PhoneNumberField(blank=True, null=True)
    comment = models.TextField(blank=True)
    address = models.TextField(blank=True)
    created = models.DateTimeField(auto_now=True)
    moder = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    last_moder = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='last_moder')
    transferred = models.BooleanField(default=False)
    transferred_date = models.DateField(blank=True, null=True)
    #actions = GenericRelation(Action)

    class Meta:
        db_table = 'partners'

    def __str__(self):
        return self.ooo

    @staticmethod
    def todayMeetList(user):
        today = datetime.date.today()
        queryset = Partner.objects.filter(moder=user, meeting_day__year=today.year, meeting_day__month=today.month,
                                          meeting_day__day=today.day)
        return queryset

    def contract_count(self):
        count = self.negotiation_set.filter(~Q(contract=None)).count()
        print(count)
        return count

    def cancelled(self):
        if self.negotiation_set.filter(status='cancelled'):
            return True
        return False

    def on_process(self):
        return self.negotiation_set.filter(~Q(status='yescontract') and ~Q(status='cancelled'))
