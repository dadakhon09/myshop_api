from django.contrib import admin

# admin.site.register(Answer)
from app.model.action import Action
from app.model.contract import Contract
from app.model.diary import Diary
from app.model.day import Day
from app.model.media_plan import MediaPlan
from app.model.negotiation import Negotiation
from app.model.partner import Partner
from app.model.payment import Payment
from app.model.process import Process
from app.model.settings import Settings
from app.model.tariff import Tariff
from app.model.users import UserProfile

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
