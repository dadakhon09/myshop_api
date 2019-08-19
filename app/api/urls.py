from django.urls import path

from app.api.action.views import ActionUpdateAPIView, ActionDeleteAPIView, ActionCreateAPIView, ActionListAPIView, \
    ActionDetailAPIView
from app.api.contract.views import ContractUpdateAPIView, ContractDeleteAPIView, ContractCreateAPIView, \
    ContractListAPIView, ContractDetailAPIView
from app.api.day.views import DayUpdateAPIView, DayDeleteAPIView, DayCreateAPIView, DayListByIdAPIView, \
    DayListByModerAPIView, DayDetailAPIView, DayGetStartedAPIView, DayGetEndedAPIView
from app.api.diary.views import DiaryUpdateAPIView, DiaryDeleteAPIView, DiaryCreateAPIView, DiaryListAPIView, DiaryDetailAPIView
from app.api.media_plan.views import MediaPlanUpdateAPIView, MediaPlanDeleteAPIView, MediaPlanCreateAPIView, \
    MediaPlanListAPIView, MediaPLanDetailAPIView
from app.api.negotiation.views import NegotiationUpdateAPIView, NegotiationDeleteAPIView, NegotiationCreateAPIView, \
    NegotiationListAPIView, NegotiationDetailAPIView
from app.api.partner.views import PartnerUpdateAPIView, PartnerTransferAPIView, PartnerDeleteAPIView, \
    PartnerCreateAPIView, PartnerListAPIView, PartnerDetailAPIView, PartnerListByModerAPIView
from app.api.payment.views import PaymentUpdateAPIView, PaymentDeleteAPIView, PaymentCreateAPIView, PaymentListAPIView, \
    PaymentDetailAPIView
from app.api.process.views import ProcessUpdateAPIView, ProcessDeleteAPIView, ProcessCreateAPIView, \
    ProcessAllListAPIView, ProcessTodayListAPIView, ProcessListByModerAPIView, ProcessDetailAPIView
from app.api.settings.views import SettingsUpdateAPIView, SettingsDeleteAPIView, SettingsCreateAPIView, \
    SettingsListAPIView, SettingsDetailAPIView
from app.api.tariff.views import TariffUpdateAPIView, TariffDeleteAPIView, TariffCreateAPIView, TariffListAPIView, \
    TariffDetailAPIView
from app.api.users.views import UserLogin, UserLogout, UserCreate, UserListAPIView


urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('create-user/', UserCreate.as_view(), name='create-user'),
    path('users/list/', UserListAPIView.as_view(), name='users-list'),
    path('partner/update/<int:id>/', PartnerUpdateAPIView.as_view(), name='partner-update'),
    path('partner/transfer/', PartnerTransferAPIView.as_view(), name='partner-transfer'),
    path('partner/delete/<int:id>/', PartnerDeleteAPIView.as_view(), name='partner-delete'),
    path('partner/create/', PartnerCreateAPIView.as_view(), name='partner-create'),
    path('partner/list/', PartnerListAPIView.as_view(), name='partner-list'),
    path('partner/list/<int:id>/', PartnerDetailAPIView.as_view(), name='partner-list-id'),
    path('partner/list/<str:slug>/', PartnerListByModerAPIView.as_view(), name='partner-list-moder'),
    path('process/update/<int:id>/', ProcessUpdateAPIView.as_view(), name='process-update'),
    path('process/delete/<int:id>/', ProcessDeleteAPIView.as_view(), name='process-delete'),
    path('process/create/', ProcessCreateAPIView.as_view(), name='process-create'),
    path('process/list/<str:slug>/today/', ProcessTodayListAPIView.as_view(), name='process-today-list'),
    path('process/list/', ProcessAllListAPIView.as_view(), name='process-all-list'),
    path('process/list/<int:id>/', ProcessDetailAPIView.as_view(), name='process-list-id'),
    path('process/list/<str:slug>/', ProcessListByModerAPIView.as_view(), name='process-list-by-moder'),
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
    path('day/list/', DayListByIdAPIView.as_view(), name='day-list'),
    path('day/list/<int:id>/', DayDetailAPIView.as_view(), name='day-list-id'),
    path('day/list/<str:slug>/', DayListByModerAPIView.as_view(), name='day-list-by-moder'),
    path('day/list/<int:id>/start/', DayGetStartedAPIView.as_view(), name='day-start'),
    path('day/list/<int:id>/end/', DayGetEndedAPIView.as_view(), name='day-end'),
    path('diary/update/<int:id>/', DiaryUpdateAPIView.as_view(), name='diary-update'),
    path('diary/delete/<int:id>/', DiaryDeleteAPIView.as_view(), name='diary-delete'),
    path('diary/create/', DiaryCreateAPIView.as_view(), name='diary-create'),
    path('diary/list/', DiaryListAPIView.as_view(), name='diary-list'),
    # path('diary/list/<str:slug>/', DiaryListByModerAPIView.as_view(), name='diary-list-by-moder'),
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
