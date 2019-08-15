from django.contrib import admin
from api.models import UserProfile, Partner, Action, Negotiation, Contract, Process, Tariff, MediaPlan, Settings, Diary, \
    Day, Payment

# admin.site.register(Answer)
admin.site.register(UserProfile)
admin.site.register(Partner)
admin.site.register(Payment)
admin.site.register(Action)
admin.site.register(Negotiation)
admin.site.register(Contract)
admin.site.register(Process)
admin.site.register(Tariff)
admin.site.register(MediaPlan)
admin.site.register(Settings)
admin.site.register(Diary)
admin.site.register(Day)
