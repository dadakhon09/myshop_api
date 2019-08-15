from rest_framework.serializers import ModelSerializer

from api.models import Tariff


class TariffCreateSerializer(ModelSerializer):
    class Meta:
        model = Tariff
        fields = ('id', 'duration', 'name')


class TariffListSerializer(ModelSerializer):
    class Meta:
        model = Tariff
        fields = ('id', 'duration', 'name')

