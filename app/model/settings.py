from django.db import models


class Settings(models.Model):
    negotiation_durability = models.CharField(max_length=10, default='2')

    class Meta:
        db_table = 'settings'

    def __str__(self):
        return self.negotiation_durability
