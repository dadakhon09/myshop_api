from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView

from api.models import Settings
from api.settings.serializers import SettingsCreateSerializer, SettingsListSerializer


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