from rest_framework.serializers import ModelSerializer

from app.api.contract.serializers import ContractListSerializer
from app.model.media_plan import MediaPlan, Document
from app.model.contract import Contract


class DocumentSerializer(ModelSerializer):

    class Meta:
        model = Document
        fields = ('id', 'document')


class MediaPlanCreateSerializer(ModelSerializer):
    class Meta:
        model = MediaPlan
        fields = ('id', 'current_month', 'description')

    # def create(self, validated_data):
    #     m = MediaPlan.objects.create(**validated_data)
    #     print('saddddddddddddd')
    #     print(validated_data)
    #     # contract_id = self.context['request'].get('contract_id')
    #     # contract = Contract.objects.get(id=1)
    #     documents = self.context['request'].FILES.getlist('documents')
    #     if documents:
    #         for d in documents:
    #             Document.objects.create(document=d, mediaplan=m)
    #     # m.contract = contract
    #     m.save()
    #     return m


class MediaPlanListSerializer(ModelSerializer):
    contract = ContractListSerializer()
    documents = DocumentSerializer(many=True, read_only=True)

    class Meta:
        model = MediaPlan
        fields = ('id', 'contract', 'current_month', 'documents', 'description', 'created')


class MediaPlanUpdateSerializer(ModelSerializer):
    documents = DocumentSerializer(many=True)

    class Meta:
        model = MediaPlan
        fields = ('id', 'current_month', 'documents', 'description')

