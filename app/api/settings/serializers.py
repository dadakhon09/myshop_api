from rest_framework.serializers import ModelSerializer

from app.model.settings import Settings


class SettingsCreateSerializer(ModelSerializer):
    class Meta:
        model = Settings
        fields = ('id', 'negotiation_durability')


class SettingsListSerializer(ModelSerializer):
    class Meta:
        model = Settings
        fields = ('id', 'negotiation_durability')

