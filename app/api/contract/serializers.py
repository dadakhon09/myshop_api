from rest_framework.serializers import ModelSerializer

from app.model.contract import Contract
from app.api.tariff.serializers import TariffListSerializer


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

