from django.contrib.auth.models import User
from django.db import models


class Day(models.Model):
    created = models.DateTimeField(auto_now=True)
    day_date = models.DateField(blank=True, null=True)
    moder = models.ForeignKey(User, related_name='day_owner', on_delete=models.CASCADE, null=True)
    done = models.BooleanField(default=False)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    @property
    def sphere(self):
        return 'Day'
    

    class Meta:
        db_table = 'days'

    def __str__(self):
        return str(self.day_date)

