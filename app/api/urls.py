from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from app.api.action.views import ActionUpdateAPIView, ActionDeleteAPIView, ActionCreateAPIView, ActionListAPIView, \
    ActionDetailAPIView, ActionListByManagerAPIView, ActionListByMediaManagerAPIView, ActionListByMediaManagerIdAPIView, \
    ActionListByManagerIdAPIView
from app.api.contract.views import ContractUpdateAPIView, ContractDeleteAPIView, ContractCreateAPIView, \
    ContractListAPIView, ContractDetailAPIView
from app.api.day.views import DayUpdateAPIView, DayDeleteAPIView, DayCreateAPIView, \
    DayListMyAPIView, DayDetailAPIView, DayGetStartedAPIView, DayGetEndedAPIView, DayListAllAPIView
from app.api.diary.views import DiaryUpdateAPIView, DiaryDeleteAPIView, DiaryCreateAPIView, DiaryListMyAPIView, \
    DiaryDetailAPIView, DiaryListTodayAPIView
from app.api.managers.views import ManagerDetailAPIView, MediaManagerDetailAPIView, MediaManagerListAPIView, \
    ManagerListAPIView
from app.api.media_plan.views import MediaPlanUpdateAPIView, MediaPlanDeleteAPIView, MediaPlanCreateAPIView, \
    MediaPlanListAPIView, MediaPLanDetailAPIView
from app.api.negotiation.views import NegotiationUpdateAPIView, NegotiationDeleteAPIView, NegotiationCreateAPIView, \
    NegotiationListAPIView, NegotiationDetailAPIView, NegotiationListByPartnerAPIView, \
    NegotiationListByDurabilityAPIView, NegotiationContractsCount
from app.api.partner.views import PartnerUpdateAPIView, PartnerTransferAPIView, PartnerDeleteAPIView, \
    PartnerCreateAPIView, PartnerListAPIView, PartnerDetailAPIView, PartnerListByModerAPIView, \
    PartnerTransferredListAPIView
from app.api.payment.views import PaymentUpdateAPIView, PaymentDeleteAPIView, PaymentCreateAPIView, PaymentListAPIView, \
    PaymentDetailAPIView
from app.api.process.views import ProcessUpdateAPIView, ProcessDeleteAPIView, ProcessCreateAPIView, \
    ProcessAllListAPIView, ProcessTodayListAPIView, ProcessListByModerAPIView, ProcessDetailAPIView, \
    EventAllListAPIView, EventMyListAPIView
from app.api.settings.views import SettingsUpdateAPIView, SettingsDeleteAPIView, SettingsCreateAPIView, \
    SettingsListAPIView, SettingsDetailAPIView
from app.api.tariff.views import TariffUpdateAPIView, TariffDeleteAPIView, TariffCreateAPIView, TariffListAPIView, \
    TariffDetailAPIView
from app.api.users.views import UserLogin, UserLogout, UserCreate, UserListAPIView, UserUpdateAPIView, UserDeleteAPIView

schema_view = get_swagger_view(title='Documentation')


urlpatterns = [
    path('doc/', schema_view, name='schema_view'),


    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('create-user/', UserCreate.as_view(), name='create-user'),
    path('users/list/', UserListAPIView.as_view(), name='users-list'),
    path('manager/list/', ManagerListAPIView.as_view(), name='managers-list'),
    path('mediamanager/list/', MediaManagerListAPIView.as_view(), name='mediamanagers-list'),
    path('manager/list/<int:id>/', ManagerDetailAPIView.as_view(), name='manager-detail'),
    path('mediamanager/list/<int:id>/', MediaManagerDetailAPIView.as_view(), name='media-manager-detail'),
    path('manager/list/<int:id>/update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('mediamanager/list/<int:id>/update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('manager/list/<int:id>/delete/', UserDeleteAPIView.as_view(), name='user-delete'),
    path('mediamanager/list/<int:id>/delete/', UserDeleteAPIView.as_view(), name='user-delete'),


    path('partner/list/<int:id>/update/', PartnerUpdateAPIView.as_view(), name='partner-update'),
    path('partner/transfer/', PartnerTransferAPIView.as_view(), name='partner-transfer'),
    path('partner/list/<int:id>/delete/', PartnerDeleteAPIView.as_view(), name='partner-delete'),
    path('partner/create/', PartnerCreateAPIView.as_view(), name='partner-create'),
    path('partner/list/all/', PartnerListAPIView.as_view(), name='partner-list'),
    path('partner/list/<int:id>/', PartnerDetailAPIView.as_view(), name='partner-list-id'),
    path('partner/list/my/', PartnerListByModerAPIView.as_view(), name='partner-list-moder'),
    path('partner/list/transferred/', PartnerTransferredListAPIView.as_view(), name='partner-list-transferred'),
    # for notification


    path('process/list/<int:id>/update/', ProcessUpdateAPIView.as_view(), name='process-update'),
    path('process/list/<int:id>/delete/', ProcessDeleteAPIView.as_view(), name='process-delete'),
    path('process/create/', ProcessCreateAPIView.as_view(), name='process-create'),
    path('process/list/today/', ProcessTodayListAPIView.as_view(), name='process-today-list'),
    path('process/list/all/', ProcessAllListAPIView.as_view(), name='process-all-list'),
    path('process/list/<int:id>/', ProcessDetailAPIView.as_view(), name='process-list-id'),
    path('process/list/my/', ProcessListByModerAPIView.as_view(), name='process-list-by-moder'),
    path('event/list/all/', EventAllListAPIView.as_view(), name='event-all-list'),
    path('event/list/my/', EventMyListAPIView.as_view(), name='event-my-list'),


    path('payment/list/<int:id>/update/', PaymentUpdateAPIView.as_view(), name='payment-update'),
    path('payment/list/<int:id>/delete/', PaymentDeleteAPIView.as_view(), name='payment-delete'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
    path('payment/list/all/', PaymentListAPIView.as_view(), name='payment-list'),
    path('payment/list/<int:id>/', PaymentDetailAPIView.as_view(), name='payment-list-id'),


    path('action/list/<int:id>/update/', ActionUpdateAPIView.as_view(), name='action-update'),
    path('action/list/<int:id>/delete/', ActionDeleteAPIView.as_view(), name='action-delete'),
    path('action/create/', ActionCreateAPIView.as_view(), name='action-create'),
    path('action/list/all/', ActionListAPIView.as_view(), name='action-list'),
    path('action/list/<int:id>/', ActionDetailAPIView.as_view(), name='action-list-id'),
    path('action/list/manager/', ActionListByManagerAPIView.as_view(), name='action-list-manager'),
    path('action/list/mediamanager/', ActionListByMediaManagerAPIView.as_view(),
         name='action-list-mediamanager'),
    path('action/list/manager/<int:id>/', ActionListByManagerIdAPIView.as_view(),
         name='action-list-manager-id'),
    path('action/list/mediamanager/<int:id>/', ActionListByMediaManagerIdAPIView.as_view(),
         name='action-list-mediamanager-id'),


    path('contract/list/<int:id>/update/', ContractUpdateAPIView.as_view(), name='contract-update'),
    path('contract/list/<int:id>/delete/', ContractDeleteAPIView.as_view(), name='contract-delete'),
    path('contract/create/', ContractCreateAPIView.as_view(), name='contract-create'),
    path('contract/list/all/', ContractListAPIView.as_view(), name='contract-list'),
    path('contract/list/<int:id>/', ContractDetailAPIView.as_view(), name='contract-list-id'),


    path('day/list/<int:id>/update/', DayUpdateAPIView.as_view(), name='day-update'),
    path('day/list/<int:id>/delete/', DayDeleteAPIView.as_view(), name='day-delete'),
    path('day/create/', DayCreateAPIView.as_view(), name='day-create'),
    path('day/list/all/', DayListAllAPIView.as_view(), name='day-list'),
    path('day/list/<int:id>/', DayDetailAPIView.as_view(), name='day-list-id'),
    path('day/list/my/', DayListMyAPIView.as_view(), name='day-list-my'),
    path('day/list/my/start/', DayGetStartedAPIView.as_view(), name='day-start'),
    path('day/list/my/end/', DayGetEndedAPIView.as_view(), name='day-end'),


    path('diary/list/<int:id>/update/', DiaryUpdateAPIView.as_view(), name='diary-update'),
    path('diary/list/<int:id>/delete/', DiaryDeleteAPIView.as_view(), name='diary-delete'),
    path('diary/create/', DiaryCreateAPIView.as_view(), name='diary-create'),
    path('diary/list/my/', DiaryListMyAPIView.as_view(), name='diary-list-my'),
    path('diary/list/today/', DiaryListTodayAPIView.as_view(), name='diary-list-today'),  # for notification
    path('diary/list/<int:id>/', DiaryDetailAPIView.as_view(), name='diary-list-id'),


    path('negotiation/list/<int:id>/update/', NegotiationUpdateAPIView.as_view(), name='negotiation-update'),
    path('negotiation/list/<int:id>/delete/', NegotiationDeleteAPIView.as_view(), name='negotiation-delete'),
    path('negotiation/create/', NegotiationCreateAPIView.as_view(), name='negotiation-create'),
    path('negotiation/list/all/', NegotiationListAPIView.as_view(), name='negotiation-list'),
    path('negotiation/list/partner/<int:id>/', NegotiationListByPartnerAPIView.as_view(),
         name='negotiation-list-by-partner'),
    path('negotiation/list/<int:id>/', NegotiationDetailAPIView.as_view(), name='negotiation-list-id'),
    path('negotiation/list/exceeded/', NegotiationListByDurabilityAPIView.as_view(), name='negotiaion-list-exceeded'),
    path('negotiation/list/partner/<int:partner_id>/contracts/', NegotiationContractsCount.as_view(), name='negotiaion-list-for-contracts-count'),


    path('tariff/list/<int:id>/update/', TariffUpdateAPIView.as_view(), name='tariff-update'),
    path('tariff/list/<int:id>/delete/', TariffDeleteAPIView.as_view(), name='tariff-delete'),
    path('tariff/create/', TariffCreateAPIView.as_view(), name='tariff-create'),
    path('tariff/list/all/', TariffListAPIView.as_view(), name='tariff-list'),
    path('tariff/list/<int:id>/', TariffDetailAPIView.as_view(), name='tariff-list-id'),


    path('mediaplan/list/<int:id>/update/', MediaPlanUpdateAPIView.as_view(), name='mediaplan-update'),
    path('mediaplan/list/<int:id>/delete/', MediaPlanDeleteAPIView.as_view(), name='mediaplan-delete'),
    path('mediaplan/create/', MediaPlanCreateAPIView.as_view(), name='mediaplan-create'),
    path('mediaplan/list/all/', MediaPlanListAPIView.as_view(), name='mediaplan-list'),
    path('mediaplan/list/<int:id>/', MediaPLanDetailAPIView.as_view(), name='mediaplan-list-id'),


    path('settings/update/<int:id>/', SettingsUpdateAPIView.as_view(), name='settings-update'),
    path('settings/list/<int:id>/delete/', SettingsDeleteAPIView.as_view(), name='settings-delete'),
    path('settings/create/', SettingsCreateAPIView.as_view(), name='settings-create'),
    path('settings/list/all/', SettingsListAPIView.as_view(), name='settings-list'),
    path('settings/list/<int:id>/', SettingsDetailAPIView.as_view(), name='settings-list-id'),
]
