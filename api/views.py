from django.shortcuts import render
from myshop_api import settings
from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth import authenticate, login, logout
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import generics, mixins
from api.models import UserProfile, Partner, Process, Payment, Action, Contract, Day, Diary, Negotiation, Tariff, \
    MediaPlan, Settings, USER_TYPES
from api.serializers import PartnerSerializer, ProcessSerializer, PaymentSerializer, ActionSerializer, \
    ContractSerializer, DaySerializer, DiarySerializer, NegotiationSerializer, TariffSerializer, MediaPlanSerializer, \
    SettingsSerializer


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


class PartnerAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = PartnerSerializer

    def get_queryset(self):
        return Partner.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PartnerRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = PartnerSerializer

    def get_queryset(self):
        return Partner.objects.all()


class ProcessAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = ProcessSerializer

    def get_queryset(self):
        return Process.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProcessRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ProcessSerializer

    def get_queryset(self):
        return Process.objects.all()


class PaymentAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PaymentRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.all()


class ActionAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = ActionSerializer

    def get_queryset(self):
        return Action.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ActionRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ActionSerializer

    def get_queryset(self):
        return Action.objects.all()


class ContractAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = ContractSerializer

    def get_queryset(self):
        return Contract.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ContractRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ContractSerializer

    def get_queryset(self):
        return Contract.objects.all()


class DayAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = DaySerializer

    def get_queryset(self):
        return Day.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DayRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = DaySerializer

    def get_queryset(self):
        return Day.objects.all()


class DiaryAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = DiarySerializer

    def get_queryset(self):
        return Diary.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DiaryRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = DiarySerializer

    def get_queryset(self):
        return Diary.objects.all()


class NegotiationAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationSerializer

    def get_queryset(self):
        return Negotiation.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NegotiationRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationSerializer

    def get_queryset(self):
        return Negotiation.objects.all()


class TariffAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = TariffSerializer

    def get_queryset(self):
        return Tariff.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TariffRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = TariffSerializer

    def get_queryset(self):
        return Tariff.objects.all()


class MediaPlanAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = MediaPlanSerializer

    def get_queryset(self):
        return MediaPlan.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MediaPlanRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = MediaPlanSerializer

    def get_queryset(self):
        return MediaPlan.objects.all()


class SettingsAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = SettingsSerializer

    def get_queryset(self):
        return Settings.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SettingsRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = SettingsSerializer

    def get_queryset(self):
        return Settings.objects.all()
