from django_cron import CronJobBase, Schedule


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 0.1
    RUN_AT_TIMES = ['17:52']

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, run_at_times=RUN_AT_TIMES)
    code = 'cron.MyCronJob'    # a unique code

    def do(self):
        print(1111111111111111111111111111111111111)
