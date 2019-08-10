from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver


# class Answer(models.Model):
#     is_correct = models.BooleanField()
#     answer_key = models.CharField(max_length=5)

#     class Meta:
#         db_table = 'answers'

#     def __str__(self):
#         return self.answer_key

#     def splitqa(self):
#         try:
#             a, b = self.answer_key
#             return a, b
#         except ValueError:
#             a, b, c = self.answer_key
#             return a, b, c

USER_TYPES = (
    (0, 'Manager'),
    (1, 'MediaManager'),
    (2, 'Admin')
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.IntegerField(null=True, blank=True, choices=USER_TYPES)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def wtf(sender, instance, **kwargs):
    UserProfile.objects.get_or_create(user=instance)


class Partner(models.Model):
    ooo = models.CharField(max_length=255, unique=True)
    contact_name = models.CharField(max_length=255, blank=True)
    stationary_phone = models.CharField(max_length=255, blank=True)
    mobile_phone = models.CharField(max_length=255, blank=True)
    comment = models.TextField(blank=True)
    address = models.TextField(blank=True)
    created = models.DateTimeField(auto_now=True)
    moder = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    last_moder = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='last_moder')
    transfered = models.BooleanField(default=False)
    transfered_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'partners'

    def __str__(self):
        return self.ooo

    @staticmethod
    def todayMeetList(user):
        today = datetime.date.today()
        queryset = Partner.objects.filter(moder=user, meeting_day__year=today.year, meeting_day__month=today.month,
                                          meeting_day__day=today.day)
        return queryset

    def contract_count(self):
        count = self.negotiation_set.filter(~Q(contract=None)).count()
        print(count)
        return count

    def cancelled(self):
        if self.negotiation_set.filter(status='cancelled'):
            return True
        return False

    def on_process(self):
        return self.negotiation_set.filter(~Q(status='yescontract') and ~Q(status='cancelled'))


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


class Negotiation(models.Model):
    created = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255, blank=True)
    contract = models.OneToOneField('Contract', on_delete=models.CASCADE, blank=True, null=True)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'negotiations'
        ordering = ['id']

    def __str__(self):
        return self.description

    def get_end_date(self):
        if self.process_set.filter(status='yescontract').count() > 0:
            return self.process_set.get(status='yescontract').created
        elif self.process_set.get(status='cancelled'):
            return self.process_set.get(status='cancelled').created
        else:
            return 'Идёт переговоры'

    def meets(self):
        today = datetime.date.today()
        if self.status == 'yescontract':
            return self.process_set.filter(status='no', destination_date__year=today.year,
                                           destination_date__month=today.month, destination_date__day=today.day)
        else:
            return self.process_set.filter(status='inprocess', destination_date__year=today.year,
                                           destination_date__month=today.month, destination_date__day=today.day)


class Contract(models.Model):
    price = models.CharField(max_length=255)
    signing_date = models.DateField(null=True, blank=True)
    activation_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    duration = models.CharField(max_length=255)
    tariff = models.ForeignKey("Tariff", on_delete=models.SET_NULL, null=True, blank=True)
    tariff_price = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'contracts'
        ordering = ['id']

    def __str__(self):
        return self.description

    def paid(self):
        paid_cash = 0
        for payment in self.payment_set.all().values('cash'):
            paid_cash += int(payment['cash'])
        return paid_cash

    def debt(self):
        return int(self.price) - self.paid()


class Process(models.Model):
    negotiation = models.ForeignKey(Negotiation, on_delete=models.CASCADE)
    cause = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)
    destination_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=255, default='empty')

    class Meta:
        db_table = 'processes'
        ordering = ['id']

    def __str__(self):
        return self.description


class Tariff(models.Model):
    duration = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'tariffs'

    def __str__(self):
        return self.name + ' ' + self.duration


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


class Payment(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    cash = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)
    pay_day = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'payments'
        ordering = ['created']

    def __str__(self):
        return self.created


class Settings(models.Model):
    negotiation_durability = models.CharField(max_length=10, default='2')

    class Meta:
        db_table = 'settings'

    def __str__(self):
        return self.negotiation_durability


class Day(models.Model):
    created = models.DateTimeField(auto_now=True)
    day_date = models.DateField(blank=True, null=True)
    moder = models.ForeignKey(User, related_name='day_owner', on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'days'

    def __str__(self):
        return str(self.day_date)


class Diary(models.Model):
    created = models.DateTimeField(auto_now=True)
    moder = models.ForeignKey(User, related_name='diary_owner', on_delete=models.CASCADE)
    cause = models.CharField(max_length=255)
    partner = models.ForeignKey(Partner, related_name='action_with', on_delete=models.CASCADE, blank=True, null=True)
    other = models.CharField(max_length=255, blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    destination_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    process = models.ForeignKey(Process, related_name='action', on_delete=models.CASCADE, blank=True, null=True)
    day = models.ForeignKey(Day, related_name='diary', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'diaries'

    def __str__(self):
        return self.cause
