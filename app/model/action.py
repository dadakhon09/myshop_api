from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.contrib.contenttypes.models import ContentType


class Action(models.Model):
    moder = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    action = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, null=True, blank=True)
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # subject = GenericForeignKey('content_type', 'object_id')
    action_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'actions'

    def __str__(self):
        return self.action
