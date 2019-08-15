from rest_framework.serializers import ModelSerializer

from api.models import Settings


class SettingsCreateSerializer(ModelSerializer):
    class Meta:
        model = Settings
        fields = ('id', 'settings')


class SettingsListSerializer(ModelSerializer):
    class Meta:
        model = Settings
        fields = ('id', 'settings')

