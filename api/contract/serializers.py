from rest_framework.serializers import ModelSerializer

from api.models import Contract
from api.tariff.serializers import TariffListSerializer


class ContractListSerializer(ModelSerializer):
    tariff = TariffListSerializer()

    class Meta:
        model = Contract
        fields = ('id', 'price', 'signing_date', 'activation_date', 'duration', 'tariff', 'tariff_price', 'description',
                  'created')


class ContractUpdateSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ('id', 'price', 'signing_date', 'activation_date', 'duration', 'tariff_price', 'description')


class ContractCreateSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ('id', 'price', 'signing_date', 'activation_date', 'duration', 'tariff', 'tariff_price', 'description')

