from rest_framework.serializers import ModelSerializer

from app.api.contract.serializers import ContractListSerializer
from app.model.negotiation import Negotiation


class NegotiationListSerializer(ModelSerializer):
    contract = ContractListSerializer()

    class Meta:
        model = Negotiation
        fields = ('id', 'created', 'description', 'contract', 'partner', 'status')


class NegotiationUpdateSerializer(ModelSerializer):
    class Meta:
        model = Negotiation
        fields = ('id', 'description', 'status')


class NegotiationCreateSerializer(ModelSerializer):
    class Meta:
        model = Negotiation
        fields = ('id', 'description', 'partner', 'status')
