from django.db import models

from app.model.contract import Contract


class MediaPlan(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    current_month = models.IntegerField()
    document = models.FileField(upload_to='')
    description = models.TextField()
    created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'mediaplans'
        ordering = ['id']

    def __str__(self):
        return self.description

