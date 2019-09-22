from datetime import datetime

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django_cron import CronJobBase, Schedule

from app.model.day import Day


class MyCronJob(CronJobBase):
    RUN_AT_TIMES = ['15:55']

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'cron.my_cron_job'

    def do(self):
        days = Day.objects.filter(end_time__isnull=True)
        print(days)
        for d in days:
            d.end_time = datetime.now()
            d.save()
