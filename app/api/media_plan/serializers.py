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

    def create(self, validated_data):
        request = self.context['request']
        contract_id = request.data.get('contract_id')
        current_month = request.data.get('current_month')
        description = request.data.get('description')
        documents = self.context['request'].FILES.getlist('documents')
        m = MediaPlan.objects.create(contract_id=int(contract_id), current_month=current_month, description=description)
        if documents:
            for d in documents:
                Document.objects.create(document=d, mediaplan=m)
        m.save()
        return m


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

