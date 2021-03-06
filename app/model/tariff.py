from django.db import models


class Tariff(models.Model):
    duration = models.CharField(max_length=255)
    name = models.CharField(max_length=255, null=True, blank=True)

    @property
    def sphere(self):
        return 'Tariff'
    
    class Meta:
        db_table = 'tariffs'

    def __str__(self):
        return self.name

