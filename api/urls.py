from django.urls import path
from api.views import UserLogin, ProcessRudView, ProcessCreateAPIView, ProcessListAPIView, \
    PaymentRudView, ActionCreateAPIView, ActionRudView, ContractRudView, DayRudView, DiaryRudView, NegotiationRudView, \
    TariffRudView, MediaPlanRudView, SettingsRudView, PartnerListAPIView, PartnerCreateAPIView, ActionListAPIView, \
    PaymentCreateAPIView, PaymentListAPIView, ContractCreateAPIView, ContractListAPIView, DayCreateAPIView, \
    DayListAPIView, DiaryCreateAPIView, DiaryListAPIView, NegotiationListAPIView, NegotiationCreateAPIView, \
    TariffCreateAPIView, TariffListAPIView, MediaPlanCreateAPIView, MediaPlanListAPIView, SettingsCreateAPIView, \
    SettingsListAPIView, PartnerUpdateAPIView, PartnerDeleteAPIView, PartnerTransferAPIView, UserListAPIView, \
    PartnerDetailAPIView, UserLogout, UserCreate

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('create-user/', UserCreate.as_view(), name='create-user'),
    path('users/list/', UserListAPIView.as_view(), name='users-list'),
    path('partner/update/<int:id>/', PartnerUpdateAPIView.as_view(), name='partner-update'),
    path('partner/transfer/<int:id>/', PartnerTransferAPIView.as_view(), name='partner-transfer'),
    path('partner/delete/<int:id>/', PartnerDeleteAPIView.as_view(), name='partner-delete'),
    path('partner/create/', PartnerCreateAPIView.as_view(), name='partner-create'),
    path('partner/list/', PartnerListAPIView.as_view(), name='partner-list'),
    path('partner/list/<int:id>/', PartnerDetailAPIView.as_view(), name='partner-list-id'),
    path('process/list/<int:id>/', ProcessRudView.as_view(), name='process-rud'),
    path('process/create/', ProcessCreateAPIView.as_view(), name='process-create'),
    path('process/list/', ProcessListAPIView.as_view(), name='process-list'),
    path('payment/list/<int:id>/', PaymentRudView.as_view(), name='payment-rud'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
    path('payment/list/', PaymentListAPIView.as_view(), name='payment-list'),
    path('action/list/<int:id>/', ActionRudView.as_view(), name='action-rud'),
    path('action/create/', ActionCreateAPIView.as_view(), name='action-create'),
    path('action/list/', ActionListAPIView.as_view(), name='action-list'),
    path('contract/list/<int:id>/', ContractRudView.as_view(), name='contract-rud'),
    path('contract/create/', ContractCreateAPIView.as_view(), name='contract-create'),
    path('contract/list/', ContractListAPIView.as_view(), name='contract-list'),
    path('day/list/<int:id>/', DayRudView.as_view(), name='day-rud'),
    path('day/create/', DayCreateAPIView.as_view(), name='day-create'),
    path('day/list/', DayListAPIView.as_view(), name='day-list'),
    path('diary/list/<int:id>/', DiaryRudView.as_view(), name='diary-rud'),
    path('diary/create/', DiaryCreateAPIView.as_view(), name='diary-create'),
    path('diary/list/', DiaryListAPIView.as_view(), name='diary-list'),
    path('negotiation/list/<int:id>/', NegotiationRudView.as_view(), name='negotiation-rud'),
    path('negotiation/create/', NegotiationCreateAPIView.as_view(), name='negotiation-create'),
    path('negotiation/list/', NegotiationListAPIView.as_view(), name='negotiation-list'),
    path('tariff/list/<int:id>/', TariffRudView.as_view(), name='tariff-rud'),
    path('tariff/create/', TariffCreateAPIView.as_view(), name='tariff-create'),
    path('tariff/list/', TariffListAPIView.as_view(), name='tariff-list'),
    path('mediaplan/list/<int:id>/', MediaPlanRudView.as_view(), name='mediaplan-rud'),
    path('mediaplan/create/', MediaPlanCreateAPIView.as_view(), name='mediaplan-create'),
    path('mediaplan/list/', MediaPlanListAPIView.as_view(), name='mediaplan-list'),
    path('settings/list/<int:id>/', SettingsRudView.as_view(), name='settings-rud'),
    path('settings/create/', SettingsCreateAPIView.as_view(), name='settings-create'),
    path('settings/list/', SettingsListAPIView.as_view(), name='settings-list'),
]
