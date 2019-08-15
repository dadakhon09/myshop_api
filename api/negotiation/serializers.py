from rest_framework.serializers import ModelSerializer

from api.contract.serializers import ContractListSerializer
from api.models import Negotiation
from api.partner.serializers import PartnerListSerializer


class NegotiationListSerializer(ModelSerializer):
    contract = ContractListSerializer()
    partner = PartnerListSerializer()

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
        fields = ('id', 'description', 'contract', 'partner', 'status')
