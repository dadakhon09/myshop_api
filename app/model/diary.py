from django.contrib.auth.models import User
from django.db import models

from app.model.day import Day
from app.model.partner import Partner
from app.model.process import Process


class Diary(models.Model):
    created = models.DateTimeField(auto_now=True)
    moder = models.ForeignKey(User, related_name='diary_owner', on_delete=models.CASCADE, null=True)
    cause = models.CharField(max_length=255)
    partner = models.ForeignKey(Partner, related_name='action_with', on_delete=models.CASCADE, blank=True, null=True)
    other = models.CharField(max_length=255, blank=True, null=True)
    result = models.TextField(blank=True, null=True, default='None')
    destination_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    process = models.ForeignKey(Process, related_name='action', on_delete=models.CASCADE, blank=True, null=True)
    day = models.ForeignKey(Day, related_name='diary', on_delete=models.CASCADE, blank=True, null=True)

    @property
    def sphere(self):
        return 'Diary'
    
    class Meta:
        db_table = 'diaries'

    def __str__(self):
        return self.cause
