from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView

from api.models import Tariff
from api.tariff.serializers import TariffCreateSerializer, TariffListSerializer


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
