from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView

from app.model.action import Action
from app.model.settings import Settings
from app.api.settings.serializers import SettingsCreateSerializer, SettingsListSerializer


class SettingsCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = SettingsCreateSerializer
    permission_classes = ()

    def get_queryset(self):
        return Settings.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(actor=self.request.user, action=f'settings {instance} created', subject=instance)


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

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(actor=self.request.user, action=f'settings {instance} updated', subject=instance)


class SettingsDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = SettingsListSerializer

    def get_queryset(self):
        return Settings.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(actor=self.request.user, action=f'settings {instance} deleted', subject=instance)


class SettingsDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = SettingsListSerializer

    def get_queryset(self):
        p = Settings.objects.filter(id=self.kwargs['id'])
        return p