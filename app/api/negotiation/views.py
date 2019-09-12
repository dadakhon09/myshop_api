from datetime import datetime, timedelta

from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from app.api.negotiation.serializers import NegotiationCreateSerializer, NegotiationListSerializer, \
    NegotiationUpdateSerializer
from app.model import Partner, Settings
from app.model.action import Action
from app.model.negotiation import Negotiation


class NegotiationCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationCreateSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Negotiation.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'negotiation {instance} created', subject=instance)


class NegotiationListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationListSerializer
    # permission_classes = (IsAuthenticated, IsAdminUser)

    def get_queryset(self):
        return Negotiation.objects.all()


class NegotiationListByDurabilityAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationListSerializer
    # permission_classes = (IsAuthenticated, IsAdminUser)

    def get_queryset(self):
        s = Settings.objects.get(id=1)
        durability = int(s.negotiation_durability)
        return Negotiation.objects.all().filter(created__lt=datetime.today() - timedelta(days=30 * durability),
                                                status__range=(0, 1))


class NegotiationListByPartnerAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationListSerializer

    def get_queryset(self):
        pk = self.kwargs['id']
        return Negotiation.objects.filter(partner_id=pk)


class NegotiationContractsCount(ListAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationListSerializer

    def get_queryset(self):
        pk = self.kwargs['partner_id']
        return Negotiation.objects.filter(partner_id=pk, status=1)


class NegotiationUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationUpdateSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Negotiation.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'negotiation {instance} updated', subject=instance)


class NegotiationDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationListSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Negotiation.objects.all()

    def perform_destroy(self, instance):
        Action.objects.create(moder=self.request.user, action=f'negotiation {instance} deleted', subject=instance)
        instance.delete()


class NegotiationDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationListSerializer

    def get_queryset(self):
        p = Negotiation.objects.filter(id=self.kwargs['id'])
        return p
