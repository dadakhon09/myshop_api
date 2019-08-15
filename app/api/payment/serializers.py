from rest_framework.serializers import ModelSerializer

from app.api.contract.serializers import ContractListSerializer
from app.model.payment import Payment


class PaymentCreateSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'contract', 'cash', 'pay_day')


class PaymentListSerializer(ModelSerializer):
    contract = ContractListSerializer()

    class Meta:
        model = Payment
        fields = ('id', 'contract', 'cash', 'created', 'pay_day')


class PaymentUpdateSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'cash', 'pay_day')
