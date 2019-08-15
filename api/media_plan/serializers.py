from rest_framework.serializers import ModelSerializer

from api.contract.serializers import ContractListSerializer
from api.models import MediaPlan


class MediaPlanCreateSerializer(ModelSerializer):
    class Meta:
        model = MediaPlan
        fields = ('id', 'contract', 'current_month', 'document', 'description')


class MediaPlanListSerializer(ModelSerializer):
    contract = ContractListSerializer()

    class Meta:
        model = MediaPlan
        fields = ('id', 'contract', 'current_month', 'document', 'description', 'created')


class MediaPlanUpdateSerializer(ModelSerializer):
    class Meta:
        model = MediaPlan
        fields = ('id', 'current_month', 'document', 'description')

