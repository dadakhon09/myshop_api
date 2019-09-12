from abc import ABC

from rest_framework.serializers import ModelSerializer, RelatedField

from app.api.contract.serializers import ContractListSerializer
from app.api.day.serializers import DayListSerializer
from app.api.diary.serializers import DiaryListSerializer
from app.api.media_plan.serializers import MediaPlanListSerializer
from app.api.negotiation.serializers import NegotiationListSerializer
from app.api.payment.serializers import PaymentListSerializer
from app.api.process.serializers import ProcessListSerializer
from app.api.settings.serializers import SettingsListSerializer
from app.api.tariff.serializers import TariffListSerializer
from app.model import Partner, Negotiation, Contract, Diary, MediaPlan, Payment, Process, Settings, Tariff
from app.model.action import Action
from app.api.partner.serializers import PartnerListSerializer
from app.api.users.serializers import UserSerializer
from app.model.day import Day


class ContentObjectRelatedField(RelatedField):
    def to_representation(self, value):
        if isinstance(value, Partner):
            serializer = PartnerListSerializer(value)
            return serializer.data
        elif isinstance(value, Negotiation):
            serializer = NegotiationListSerializer(value)
            return {'Negotiation': f'{serializer.data}'}
        elif isinstance(value, Contract):
            serializer = ContractListSerializer(value)
            return {'Contract': f'{serializer.data}'}
        elif isinstance(value, Day):
            serializer = DayListSerializer(value)
            return {'Day': f'{serializer.data}'}
        elif isinstance(value, Diary):
            serializer = DiaryListSerializer(value)
            return {'Diary': f'{serializer.data}'}
        elif isinstance(value, MediaPlan):
            serializer = MediaPlanListSerializer(value)
            return {'MediaPlan': f'{serializer.data}'}
        elif isinstance(value, Payment):
            serializer = PaymentListSerializer(value)
            return {'Payment': f'{serializer.data}'}
        elif isinstance(value, Process):
            serializer = ProcessListSerializer(value)
            return {'Process': f'{serializer.data}'}
        elif isinstance(value, Settings):
            serializer = SettingsListSerializer(value)
            return {'Settings': f'{serializer.data}'}
        elif isinstance(value, Tariff):
            serializer = TariffListSerializer(value)
            return {'Tariff': f'{serializer.data}'}
        else:
            raise Exception('Unexpected type of tagged object')

    def get_queryset(self):
        return None


class ActionListSerializer(ModelSerializer):
    moder = UserSerializer()
    subject = ContentObjectRelatedField()

    class Meta:
        model = Action
        fields = ('id', 'moder', 'action', 'subject', 'action_date')


class ActionCreateSerializer(ModelSerializer):
    class Meta:
        model = Action
        fields = ('id', 'action', 'subject')

    def create(self, validated_data):
        a = Action.objects.create(**validated_data)
        return a


class ActionUpdateSerializer(ModelSerializer):
    class Meta:
        model = Action
        fields = ('id', 'action')

