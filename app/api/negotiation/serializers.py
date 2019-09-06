from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from app.api.contract.serializers import ContractListSerializer
from app.model import Process
from app.model.negotiation import Negotiation


class NegotiationListSerializer(ModelSerializer):
    contract = ContractListSerializer()
    end_date = SerializerMethodField('get_end_date')

    class Meta:
        model = Negotiation
        fields = ('id', 'created', 'end_date', 'description', 'contract', 'partner', 'status')

    def get_end_date(self, obj):
        processes = Process.objects.filter(negotiation_id=obj.id, status__range=(1, 2))
        obj.status = 0
        for p in processes:
            end = p.created
            if p.status == 1:
                obj.status = 1
            elif p.status == 2:
                obj.status = 2
            obj.save()
            return end


class NegotiationUpdateSerializer(ModelSerializer):
    class Meta:
        model = Negotiation
        fields = ('id', 'description', 'status')


class NegotiationCreateSerializer(ModelSerializer):
    class Meta:
        model = Negotiation
        fields = ('id', 'description', 'partner', 'status')
