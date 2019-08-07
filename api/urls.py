from django.urls import path
from api.views import home,UserLogin, PartnerRudView, PartnerAPIView, ProcessRudView, ProcessAPIView, PaymentAPIView, PaymentRudView, ActionAPIView, ActionRudView, ContractRudView, ContractAPIView, DayRudView, DayAPIView, DiaryAPIView, DiaryRudView, NegotiationRudView, NegotiationAPIView, TariffAPIView, TariffRudView, MediaPlanAPIView, MediaPlanRudView, SettingsAPIView, SettingsRudView
from api.models import Partner, Process, Payment, Action, Contract, Day, Diary, Negotiation, Tariff, MediaPlan, Settings


urlpatterns = [
    path('', home, name='home'),
    path('login/', UserLogin.as_view(), name='login'),
    path('partner/<int:id>/', PartnerRudView.as_view(), name='partner-rud'),
    path('partner/create', PartnerAPIView.as_view(), name='partner-create'),
    path('process/<int:id>/', ProcessRudView.as_view(), name='process-rud'),
    path('process/create', ProcessAPIView.as_view(), name='process-create'),
    path('payment/<int:id>/', PaymentRudView.as_view(), name='payment-rud'),
    path('payment/create', PaymentAPIView.as_view(), name='payment-create'),
    path('action/<int:id>/', ActionRudView.as_view(), name='action-rud'),
    path('action/create', ActionAPIView.as_view(), name='action-create'),
    path('contract/<int:id>/', ContractRudView.as_view(), name='contract-rud'),
    path('contract/create', ContractAPIView.as_view(), name='contract-create'),
    path('day/<int:id>/', DayRudView.as_view(), name='day-rud'),
    path('day/create', DayAPIView.as_view(), name='day-create'),
    path('diary/<int:id>/', DiaryRudView.as_view(), name='diary-rud'),
    path('diary/create', DiaryAPIView.as_view(), name='diary-create'),
    path('negotiation/<int:id>/', NegotiationRudView.as_view(), name='negotiation-rud'),
    path('negotiation/create', NegotiationAPIView.as_view(), name='negotiation-create'),
    path('tariff/<int:id>/', TariffRudView.as_view(), name='tariff-rud'),
    path('tariff/create', TariffAPIView.as_view(), name='tariff-create'),
    path('mediaplan/<int:id>/', MediaPlanRudView.as_view(), name='mediaplan-rud'),
    path('mediaplan/create', MediaPlanAPIView.as_view(), name='mediaplan-create'),
    path('settings/<int:id>/', SettingsRudView.as_view(), name='settings-rud'),
    path('settings/create', SettingsAPIView.as_view(), name='settings-create'),
]

