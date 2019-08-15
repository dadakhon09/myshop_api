from django.urls import path
from api.views import UserLogin, ProcessCreateAPIView, ProcessListAPIView, ActionCreateAPIView, \
    PartnerListAPIView, PartnerCreateAPIView, ActionListAPIView, \
    PaymentCreateAPIView, PaymentListAPIView, ContractCreateAPIView, ContractListAPIView, DayCreateAPIView, \
    DayListAPIView, DiaryCreateAPIView, DiaryListAPIView, NegotiationListAPIView, NegotiationCreateAPIView, \
    TariffCreateAPIView, TariffListAPIView, MediaPlanCreateAPIView, MediaPlanListAPIView, SettingsCreateAPIView, \
    SettingsListAPIView, PartnerUpdateAPIView, PartnerDeleteAPIView, PartnerTransferAPIView, UserListAPIView, \
    PartnerDetailAPIView, UserLogout, UserCreate, ProcessUpdateAPIView, ProcessDeleteAPIView, PaymentDeleteAPIView, \
    PaymentUpdateAPIView, ActionUpdateAPIView, ActionDeleteAPIView, ContractUpdateAPIView, ContractDeleteAPIView, \
    DayUpdateAPIView, DayDeleteAPIView, DiaryUpdateAPIView, DiaryDeleteAPIView, NegotiationUpdateAPIView, \
    NegotiationDeleteAPIView, TariffUpdateAPIView, TariffDeleteAPIView, MediaPlanUpdateAPIView, MediaPlanDeleteAPIView, \
    SettingsUpdateAPIView, SettingsDeleteAPIView, ProcessDetailAPIView, PaymentDetailAPIView, ActionDetailAPIView, \
    ContractDetailAPIView, DayDetailAPIView, DiaryDetailAPIView, NegotiationDetailAPIView, TariffDetailAPIView, \
    SettingsDetailAPIView, MediaPLanDetailAPIView

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
    path('process/update/<int:id>/', ProcessUpdateAPIView.as_view(), name='process-update'),
    path('process/delete/<int:id>/', ProcessDeleteAPIView.as_view(), name='process-delete'),
    path('process/create/', ProcessCreateAPIView.as_view(), name='process-create'),
    path('process/list/', ProcessListAPIView.as_view(), name='process-list'),
    path('process/list/<int:id>/', ProcessDetailAPIView.as_view(), name='process-list-id'),
    path('payment/update/<int:id>/', PaymentUpdateAPIView.as_view(), name='payment-update'),
    path('payment/delete/<int:id>/', PaymentDeleteAPIView.as_view(), name='payment-delete'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
    path('payment/list/', PaymentListAPIView.as_view(), name='payment-list'),
    path('payment/list/<int:id>/', PaymentDetailAPIView.as_view(), name='payment-list-id'),
    path('action/update/<int:id>/', ActionUpdateAPIView.as_view(), name='action-update'),
    path('action/delete/<int:id>/', ActionDeleteAPIView.as_view(), name='action-delete'),
    path('action/create/', ActionCreateAPIView.as_view(), name='action-create'),
    path('action/list/', ActionListAPIView.as_view(), name='action-list'),
    path('action/list/<int:id>/', ActionDetailAPIView.as_view(), name='action-list-id'),
    path('contract/update/<int:id>/', ContractUpdateAPIView.as_view(), name='contract-update'),
    path('contract/delete/<int:id>/', ContractDeleteAPIView.as_view(), name='contract-delete'), 
    path('contract/create/', ContractCreateAPIView.as_view(), name='contract-create'),
    path('contract/list/', ContractListAPIView.as_view(), name='contract-list'),
    path('contract/list/<int:id>/', ContractDetailAPIView.as_view(), name='contract-list-id'),
    path('day/update/<int:id>/', DayUpdateAPIView.as_view(), name='day-update'),
    path('day/delete/<int:id>/', DayDeleteAPIView.as_view(), name='day-delete'),
    path('day/create/', DayCreateAPIView.as_view(), name='day-create'),
    path('day/list/', DayListAPIView.as_view(), name='day-list'),
    path('day/list/<int:id>/', DayDetailAPIView.as_view(), name='day-list-id'),
    path('diary/update/<int:id>/', DiaryUpdateAPIView.as_view(), name='diary-update'),
    path('diary/delete/<int:id>/', DiaryDeleteAPIView.as_view(), name='diary-delete'),
    path('diary/create/', DiaryCreateAPIView.as_view(), name='diary-create'),
    path('diary/list/', DiaryListAPIView.as_view(), name='diary-list'),
    path('diary/list/<int:id>/', DiaryDetailAPIView.as_view(), name='diary-list-id'),
    path('negotiation/update/<int:id>/', NegotiationUpdateAPIView.as_view(), name='negotiation-update'),
    path('negotiation/delete/<int:id>/', NegotiationDeleteAPIView.as_view(), name='negotiation-delete'),
    path('negotiation/create/', NegotiationCreateAPIView.as_view(), name='negotiation-create'),
    path('negotiation/list/', NegotiationListAPIView.as_view(), name='negotiation-list'),
    path('negotiation/list/<int:id>/', NegotiationDetailAPIView.as_view(), name='negotiation-list-id'),
    path('tariff/update/<int:id>/', TariffUpdateAPIView.as_view(), name='tariff-update'),
    path('tariff/delete/<int:id>/', TariffDeleteAPIView.as_view(), name='tariff-delete'),
    path('tariff/create/', TariffCreateAPIView.as_view(), name='tariff-create'),
    path('tariff/list/', TariffListAPIView.as_view(), name='tariff-list'),
    path('tariff/list/<int:id>/', TariffDetailAPIView.as_view(), name='tariff-list-id'),
    path('mediaplan/update/<int:id>/', MediaPlanUpdateAPIView.as_view(), name='mediaplan-update'),
    path('mediaplan/delete/<int:id>/', MediaPlanDeleteAPIView.as_view(), name='mediaplan-delete'),
    path('mediaplan/create/', MediaPlanCreateAPIView.as_view(), name='mediaplan-create'),
    path('mediaplan/list/', MediaPlanListAPIView.as_view(), name='mediaplan-list'),
    path('mediaplan/list/<int:id>/', MediaPLanDetailAPIView.as_view(), name='mediaplan-list-id'),
    path('settings/update/<int:id>/', SettingsUpdateAPIView.as_view(), name='settings-update'),
    path('settings/delete/<int:id>/', SettingsDeleteAPIView.as_view(), name='settings-delete'),
    path('settings/create/', SettingsCreateAPIView.as_view(), name='settings-create'),
    path('settings/list/', SettingsListAPIView.as_view(), name='settings-list'),
    path('settings/list/<int:id>/', SettingsDetailAPIView.as_view(), name='settings-list-id'),

]
