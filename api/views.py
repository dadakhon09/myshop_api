from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.contrib.auth import authenticate
# from .pagination import UserPageNumberPagination
from rest_framework.pagination import PageNumberPagination

from api.models import UserProfile, Partner, Process, Payment, Action, Contract, Day, Diary, Negotiation, Tariff, \
    MediaPlan, Settings
from api.serializers import PartnerListSerializer, PartnerCreateSerializer, \
    ActionCreateSerializer, ActionListSerializer, ProcessCreateSerializer, ProcessListSerializer, \
    ContractCreateSerializer, ContractListSerializer, PaymentListSerializer, PaymentCreateSerializer, \
    DayCreateSerializer, DayListSerializer, DiaryCreateSerializer, DiaryListSerializer, NegotiationCreateSerializer, \
    NegotiationListSerializer, TariffCreateSerializer, TariffListSerializer, MediaPlanCreateSerializer, \
    MediaPlanListSerializer, SettingsCreateSerializer, SettingsListSerializer, PartnerTransferSerializer, \
    PartnerUpdateSerializer, UserProfileSerializer, MediaPlanUpdateSerializer, NegotiationUpdateSerializer, \
    DiaryUpdateSerializer, DayUpdateSerializer, ContractUpdateSerializer, ActionUpdateSerializer, \
    PaymentUpdateSerializer, ProcessUpdateSerializer


def home(request):
    return render(request, 'home.html')


@permission_classes((IsAdminUser,))
class UserCreate(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        type = data['type']

        user_check = User.objects.filter(username=username)
        if not user_check:
            new_user = User.objects.create_user(username, password)
            token, _ = Token.objects.get_or_create(user=new_user)
            new_user.userprofile.type = type
            new_user.userprofile.save()
            new_user.save()
            return Response("User is created")
        else:
            return Response("We have already the same username")


@permission_classes((AllowAny,))
class UserLogin(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password!'})
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid credentials!'})
        token, _ = Token.objects.get_or_create(user=user)
        profile = UserProfile.objects.get(user=user)
        return Response({'token': token.key,
                         'user_id': user.id,
                         'username': user.username,
                         'is_superuser': user.is_superuser,
                         'user_type': profile.get_type_display()})


@permission_classes((IsAuthenticated,))
class UserLogout(APIView):
    def get(self, request, format=None):
        if request.user:
            request.user.auth_token.delete()
        else:
            Response("Please login first")
        return Response("Successfully logged out")


class UserListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class PartnerCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = PartnerCreateSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.moder = self.request.user
        instance.save()


class PartnerListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = PartnerListSerializer
    queryset = Partner.objects.all().order_by('id')


class PartnerDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = PartnerListSerializer

    def get_queryset(self):
        p = Partner.objects.filter(id=self.kwargs['id'])
        return p


class PartnerTransferAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = PartnerTransferSerializer

    def get_queryset(self):
        return Partner.objects.all()


class PartnerUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = PartnerUpdateSerializer

    def get_queryset(self):
        return Partner.objects.all()


class PartnerDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = PartnerListSerializer

    def get_queryset(self):
        return Partner.objects.all()


class ProcessCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = ProcessCreateSerializer


class ProcessListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ProcessListSerializer
    queryset = Process.objects.all()


class ProcessUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = ProcessUpdateSerializer

    def get_queryset(self):
        return Partner.objects.all()


class ProcessDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ProcessListSerializer

    def get_queryset(self):
        return Partner.objects.all()


class ProcessDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ProcessListSerializer

    def get_queryset(self):
        p = Process.objects.filter(id=self.kwargs['id'])
        return p


class PaymentCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = PaymentCreateSerializer

    def get_queryset(self):
        return Payment.objects.all()


class PaymentListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = PaymentListSerializer

    def get_queryset(self):
        return Payment.objects.all()


class PaymentUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = PaymentUpdateSerializer

    def get_queryset(self):
        return Payment.objects.all()


class PaymentDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = PaymentListSerializer

    def get_queryset(self):
        return Payment.objects.all()


class PaymentDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = PaymentListSerializer

    def get_queryset(self):
        p = Payment.objects.filter(id=self.kwargs['id'])
        return p


class ActionCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = ActionCreateSerializer
    queryset = Action.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.actor = self.request.user
        instance.save()


class ActionListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ActionListSerializer
    queryset = Action.objects.all()


class ActionUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = ActionUpdateSerializer

    def get_queryset(self):
        return Action.objects.all()


class ActionDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ActionListSerializer

    def get_queryset(self):
        return Action.objects.all()


class ActionDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ActionListSerializer

    def get_queryset(self):
        p = Action.objects.filter(id=self.kwargs['id'])
        return p


class ContractCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = ContractCreateSerializer

    def get_queryset(self):
        return Contract.objects.all()


class ContractListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ContractListSerializer

    def get_queryset(self):
        return Contract.objects.all()


class ContractUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = ContractUpdateSerializer

    def get_queryset(self):
        return Contract.objects.all()


class ContractDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ContractListSerializer

    def get_queryset(self):
        return Contract.objects.all()


class ContractDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ContractListSerializer

    def get_queryset(self):
        p = Contract.objects.filter(id=self.kwargs['id'])
        return p


class DayCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = DayCreateSerializer

    def get_queryset(self):
        return Day.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.moder = self.request.user
        instance.save()


class DayListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = DayListSerializer

    def get_queryset(self):
        return Day.objects.all()


class DayUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = DayUpdateSerializer

    def get_queryset(self):
        return Day.objects.all()


class DayDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = DayListSerializer

    def get_queryset(self):
        return Day.objects.all()


class DayDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = DayListSerializer

    def get_queryset(self):
        p = Day.objects.filter(id=self.kwargs['id'])
        return p


class DiaryCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = DiaryCreateSerializer

    def get_queryset(self):
        return Diary.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.moder = self.request.user
        instance.save()


class DiaryListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = DiaryListSerializer

    def get_queryset(self):
        return Diary.objects.all()


class DiaryUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = DiaryUpdateSerializer

    def get_queryset(self):
        return Diary.objects.all()


class DiaryDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = DiaryListSerializer

    def get_queryset(self):
        return Diary.objects.all()


class DiaryDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = DiaryListSerializer

    def get_queryset(self):
        p = Diary.objects.filter(id=self.kwargs['id'])
        return p


class NegotiationCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationCreateSerializer

    def get_queryset(self):
        return Negotiation.objects.all()


class NegotiationListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationListSerializer

    def get_queryset(self):
        return Negotiation.objects.all()


class NegotiationUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationUpdateSerializer

    def get_queryset(self):
        return Negotiation.objects.all()


class NegotiationDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationListSerializer

    def get_queryset(self):
        return Negotiation.objects.all()


class NegotiationDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationListSerializer

    def get_queryset(self):
        p = Negotiation.objects.filter(id=self.kwargs['id'])
        return p


class TariffCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = TariffCreateSerializer

    def get_queryset(self):
        return Tariff.objects.all()


class TariffListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = TariffListSerializer

    def get_queryset(self):
        return Tariff.objects.all()


class TariffUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = TariffListSerializer

    def get_queryset(self):
        return Tariff.objects.all()


class TariffDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = TariffListSerializer

    def get_queryset(self):
        return Tariff.objects.all()


class TariffDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = TariffListSerializer

    def get_queryset(self):
        p = Tariff.objects.filter(id=self.kwargs['id'])
        return p


class MediaPlanCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = MediaPlanCreateSerializer

    def get_queryset(self):
        return MediaPlan.objects.all()


class MediaPlanListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = MediaPlanListSerializer

    def get_queryset(self):
        return MediaPlan.objects.all()


class MediaPlanUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = MediaPlanUpdateSerializer

    def get_queryset(self):
        return MediaPlan.objects.all()


class MediaPlanDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = MediaPlanListSerializer

    def get_queryset(self):
        return MediaPlan.objects.all()


class MediaPLanDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = MediaPlanListSerializer

    def get_queryset(self):
        p = MediaPlan.objects.filter(id=self.kwargs['id'])
        return p


class SettingsCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = SettingsCreateSerializer

    def get_queryset(self):
        return Settings.objects.all()


class SettingsListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = SettingsListSerializer

    def get_queryset(self):
        return Settings.objects.all()


class SettingsUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = SettingsListSerializer

    def get_queryset(self):
        return Settings.objects.all()


class SettingsDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = SettingsListSerializer

    def get_queryset(self):
        return Settings.objects.all()


class SettingsDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = SettingsListSerializer

    def get_queryset(self):
        p = Settings.objects.filter(id=self.kwargs['id'])
        return p