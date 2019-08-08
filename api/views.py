from django.shortcuts import render
from myshop_api import settings
from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, mixins
from api.models import UserProfile, Partner, Process, Payment, Action, Contract, Day, Diary, Negotiation, Tariff, \
    MediaPlan, Settings, USER_TYPES
from api.serializers import PartnerListSerializer, PartnerCreateSerializer, \
    ActionCreateSerializer, ActionListSerializer, ProcessCreateSerializer, ProcessListSerializer, \
    ContractCreateSerializer, ContractListSerializer, PaymentListSerializer, PaymentCreateSerializer, \
    DayCreateSerializer, DayListSerializer, DiaryCreateSerializer, DiaryListSerializer, NegotiationCreateSerializer, \
    NegotiationListSerializer, TariffCreateSerializer, TariffListSerializer, MediaPlanCreateSerializer, \
    MediaPlanListSerializer, SettingsCreateSerializer, SettingsListSerializer, PartnerRUDSerializer


def home(request):
    return render(request, 'home.html')


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


class PartnerCreateAPIView(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = PartnerCreateSerializer


class PartnerListAPIView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = PartnerListSerializer
    queryset = Partner.objects.all()


class PartnerRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = PartnerRUDSerializer

    def get_queryset(self):
        return Partner.objects.all()


class ProcessCreateAPIView(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = ProcessCreateSerializer


class ProcessListAPIView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = ProcessListSerializer
    queryset = Process.objects.all()


class ProcessRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ProcessListSerializer

    def get_queryset(self):
        return Process.objects.all()


class PaymentCreateAPIView(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = PaymentCreateSerializer

    def get_queryset(self):
        return Payment.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = PaymentListSerializer

    def get_queryset(self):
        return Payment.objects.all()


class PaymentRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = PaymentListSerializer

    def get_queryset(self):
        return Payment.objects.all()


class ActionCreateAPIView(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = ActionCreateSerializer
    queryset = Action.objects.all()


class ActionListAPIView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = ActionListSerializer
    queryset = Action.objects.all()


class ActionRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ActionListSerializer

    def get_queryset(self):
        return Action.objects.all()


class ContractCreateAPIView(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = ContractCreateSerializer

    def get_queryset(self):
        return Contract.objects.all()


class ContractListAPIView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = ContractListSerializer

    def get_queryset(self):
        return Contract.objects.all()


class ContractRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ContractListSerializer

    def get_queryset(self):
        return Contract.objects.all()


class DayCreateAPIView(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = DayCreateSerializer

    def get_queryset(self):
        return Day.objects.all()


class DayListAPIView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = DayListSerializer

    def get_queryset(self):
        return Day.objects.all()


class DayRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = DayListSerializer

    def get_queryset(self):
        return Day.objects.all()


class DiaryCreateAPIView(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = DiaryCreateSerializer

    def get_queryset(self):
        return Diary.objects.all()


class DiaryListAPIView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = DiaryListSerializer

    def get_queryset(self):
        return Diary.objects.all()


class DiaryRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = DiaryListSerializer

    def get_queryset(self):
        return Diary.objects.all()


class NegotiationCreateAPIView(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationCreateSerializer

    def get_queryset(self):
        return Negotiation.objects.all()


class NegotiationListAPIView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationListSerializer

    def get_queryset(self):
        return Negotiation.objects.all()


class NegotiationRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationListSerializer

    def get_queryset(self):
        return Negotiation.objects.all()


class TariffCreateAPIView(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = TariffCreateSerializer

    def get_queryset(self):
        return Tariff.objects.all()


class TariffListAPIView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = TariffListSerializer

    def get_queryset(self):
        return Tariff.objects.all()


class TariffRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = TariffListSerializer

    def get_queryset(self):
        return Tariff.objects.all()


class MediaPlanCreateAPIView(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = MediaPlanCreateSerializer

    def get_queryset(self):
        return MediaPlan.objects.all()


class MediaPlanListAPIView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = MediaPlanListSerializer

    def get_queryset(self):
        return MediaPlan.objects.all()


class MediaPlanRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = MediaPlanListSerializer

    def get_queryset(self):
        return MediaPlan.objects.all()


class SettingsCreateAPIView(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = SettingsCreateSerializer

    def get_queryset(self):
        return Settings.objects.all()


class SettingsListAPIView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = SettingsListSerializer

    def get_queryset(self):
        return Settings.objects.all()


class SettingsRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = SettingsListSerializer

    def get_queryset(self):
        return Settings.objects.all()
