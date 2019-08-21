from django.contrib.auth.models import User
from django.db import models


class Action(models.Model):
    moder = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    action = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    action_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'actions'

    def __str__(self):
        return self.action
