from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView

from app.model.action import Action
from app.model.tariff import Tariff
from app.api.tariff.serializers import TariffCreateSerializer, TariffListSerializer


class TariffCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = TariffCreateSerializer
    permission_classes = ()

    def get_queryset(self):
        return Tariff.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(actor=self.request.user, action=f'tariff {instance} created', subject=instance)


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

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(actor=self.request.user, action=f'tariff {instance} updated', subject=instance)


class TariffDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = TariffListSerializer

    def get_queryset(self):
        return Tariff.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(actor=self.request.user, action=f'tariff {instance} deleted', subject=instance)


class TariffDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = TariffListSerializer

    def get_queryset(self):
        p = Tariff.objects.filter(id=self.kwargs['id'])
        return p
