from rest_framework.serializers import ModelSerializer

from app.api.contract.serializers import ContractListSerializer
from app.model.media_plan import MediaPlan, Document


class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'document')


class MediaPlanCreateSerializer(ModelSerializer):
    class Meta:
        model = MediaPlan
        fields = ('id', 'contract', 'current_month', 'description')

    def create(self, validated_data):
        m = MediaPlan.objects.create(**validated_data)
        documents = self.context['request'].FILES.getlist('documents')
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

