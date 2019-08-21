from django.urls import path

from app.api.action.views import ActionUpdateAPIView, ActionDeleteAPIView, ActionCreateAPIView, ActionListAPIView, \
    ActionDetailAPIView
from app.api.contract.views import ContractUpdateAPIView, ContractDeleteAPIView, ContractCreateAPIView, \
    ContractListAPIView, ContractDetailAPIView
from app.api.day.views import DayUpdateAPIView, DayDeleteAPIView, DayCreateAPIView, DayListByIdAPIView, \
    DayListByModerAPIView, DayDetailAPIView, DayGetStartedAPIView, DayGetEndedAPIView
from app.api.diary.views import DiaryUpdateAPIView, DiaryDeleteAPIView, DiaryCreateAPIView, DiaryListMyAPIView, \
    DiaryDetailAPIView, DiaryListTodayAPIView
from app.api.media_plan.views import MediaPlanUpdateAPIView, MediaPlanDeleteAPIView, MediaPlanCreateAPIView, \
    MediaPlanListAPIView, MediaPLanDetailAPIView
from app.api.negotiation.views import NegotiationUpdateAPIView, NegotiationDeleteAPIView, NegotiationCreateAPIView, \
    NegotiationListAPIView, NegotiationDetailAPIView
from app.api.partner.views import PartnerUpdateAPIView, PartnerTransferAPIView, PartnerDeleteAPIView, \
    PartnerCreateAPIView, PartnerListAPIView, PartnerDetailAPIView, PartnerListByModerAPIView, \
    PartnerTransferredListAPIView
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
    path('create-user/', UserCreate.as_view(), name='create-user'), # for admin
    path('users/list/', UserListAPIView.as_view(), name='users-list'), # all users list 
    path('partner/update/<int:id>/', PartnerUpdateAPIView.as_view(), name='partner-update'), # edit  one partner by id 
    path('partner/transfer/', PartnerTransferAPIView.as_view(), name='partner-transfer'), # one or more 'partner' to 1 'user_id' 
    path('partner/delete/<int:id>/', PartnerDeleteAPIView.as_view(), name='partner-delete'), # delete one partner by id (admin can delete all partners, when manager can only delete his/her partners only, media managers can not delete any partner )
    path('partner/create/', PartnerCreateAPIView.as_view(), name='partner-create'), # only admin and manager (not media manager)
    path('partner/list/all/', PartnerListAPIView.as_view(), name='partner-list'), # for admin
    path('partner/list/<int:id>/', PartnerDetailAPIView.as_view(), name='partner-list-id'), #  one partner detail
    path('partner/list/my/', PartnerListByModerAPIView.as_view(), name='partner-list-moder'),# one's partner list
    path('partner/list/transferred/', PartnerTransferredListAPIView.as_view(), name='partner-list-transferred'),  # for notification
    path('process/update/<int:id>/', ProcessUpdateAPIView.as_view(), name='process-update'), 
    path('process/delete/<int:id>/', ProcessDeleteAPIView.as_view(), name='process-delete'),
    path('process/create/', ProcessCreateAPIView.as_view(), name='process-create'), #'partner'
    path('process/list/today/', ProcessTodayListAPIView.as_view(), name='process-today-list'),
    path('process/list/', ProcessAllListAPIView.as_view(), name='process-all-list'),
    path('process/list/<int:id>/', ProcessDetailAPIView.as_view(), name='process-list-id'),
    path('process/list/my/', ProcessListByModerAPIView.as_view(), name='process-list-by-moder'),
    path('payment/update/<int:id>/', PaymentUpdateAPIView.as_view(), name='payment-update'),
    path('payment/delete/<int:id>/', PaymentDeleteAPIView.as_view(), name='payment-delete'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
    path('payment/list/', PaymentListAPIView.as_view(), name='payment-list'),
    path('payment/list/<int:id>/', PaymentDetailAPIView.as_view(), name='payment-list-id'),
    path('action/update/<int:id>/', ActionUpdateAPIView.as_view(), name='action-update'), #---
    path('action/delete/<int:id>/', ActionDeleteAPIView.as_view(), name='action-delete'),# ---
    path('action/create/', ActionCreateAPIView.as_view(), name='action-create'),#---
    path('action/list/', ActionListAPIView.as_view(), name='action-list'),# all actions for admin (Logi)
    path('action/list/<int:id>/', ActionDetailAPIView.as_view(), name='action-list-id'),#---
    path('contract/update/<int:id>/', ContractUpdateAPIView.as_view(), name='contract-update'),# edit contract only media managers
    path('contract/delete/<int:id>/', ContractDeleteAPIView.as_view(), name='contract-delete'),# Delete contract visually media manager  
    path('contract/create/', ContractCreateAPIView.as_view(), name='contract-create'),# media manager
    path('contract/list/', ContractListAPIView.as_view(), name='contract-list'),# media manager
    path('contract/list/<int:id>/', ContractDetailAPIView.as_view(), name='contract-list-id'),#contract list by id
    path('day/update/<int:id>/', DayUpdateAPIView.as_view(), name='day-update'),#WTF
    path('day/delete/<int:id>/', DayDeleteAPIView.as_view(), name='day-delete'),#WTF
    path('day/create/', DayCreateAPIView.as_view(), name='day-create'),# automatic
    path('day/list/', DayListByIdAPIView.as_view(), name='day-list'),#---
    path('day/list/<int:id>/', DayDetailAPIView.as_view(), name='day-list-id'),#---
    path('day/list/my/', DayListByModerAPIView.as_view(), name='day-list-by-moder'),
    path('day/list/<int:id>/start/', DayGetStartedAPIView.as_view(), name='day-start'),
    path('day/list/<int:id>/end/', DayGetEndedAPIView.as_view(), name='day-end'),
    path('diary/update/<int:id>/', DiaryUpdateAPIView.as_view(), name='diary-update'),
    path('diary/delete/<int:id>/', DiaryDeleteAPIView.as_view(), name='diary-delete'),
    path('diary/create/', DiaryCreateAPIView.as_view(), name='diary-create'),
    path('diary/list/my/', DiaryListMyAPIView.as_view(), name='diary-list-my'),
    path('diary/list/today/', DiaryListTodayAPIView.as_view(), name='diary-list-today'),  # for notification
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
