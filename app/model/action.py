from django.contrib.auth.models import User
from django.db import models

from app.model.partner import Partner


class Action(models.Model):
    actor = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    action = models.CharField(max_length=255)
    subject = models.ForeignKey(Partner, blank=True, null=True, on_delete=models.SET_NULL)
    action_date = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'actions'

    def __str__(self):
        return self.action

