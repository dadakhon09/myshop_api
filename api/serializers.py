from rest_framework import serializers
from api.models import Partner, Process, Payment, Action, Contract, Day, Diary, Negotiation, Tariff, MediaPlan, Settings


class PartnerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = (
            'id', 'ooo', 'contact_name', 'stationary_phone', 'mobile_phone', 'comment', 'address', 'created', 'moder',
            'last_moder', 'transfered', 'transfered_date')


class PartnerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = (
            'id', 'ooo', 'contact_name', 'stationary_phone', 'mobile_phone', 'comment', 'address', 'moder',
            'last_moder', 'transfered', 'transfered_date')

    def create(self, validated_data):
        p = Partner.objects.create(**validated_data)
        return p


class ActionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ('id', 'actor', 'action', 'subject', 'action_date', 'comment')


class ActionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ('id', 'actor', 'action', 'subject', 'comment')

    def create(self, validated_data):
        a = Action.objects.create(**validated_data)
        return a


class ContractListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('id', 'price', 'signing_date', 'activation_date', 'duration', 'tariff', 'tariff_price', 'description',
                  'created')


class ContractCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('id', 'price', 'signing_date', 'activation_date', 'duration', 'tariff', 'tariff_price', 'description')


class NegotiationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negotiation
        fields = ('id', 'created', 'description', 'contract', 'partner', 'status')


class NegotiationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negotiation
        fields = ('id', 'description', 'contract', 'partner', 'status')


class ProcessCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = ('id', 'negotiation', 'cause', 'destination_date', 'description', 'status')


class ProcessListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = ('id', 'negotiation', 'cause', 'created', 'destination_date', 'description', 'status')


class TariffCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = ('id', 'duration', 'name')


class TariffListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = ('id', 'duration', 'name')


class MediaPlanCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaPlan
        fields = ('id', 'contract', 'current_month', 'document', 'description')


class MediaPlanListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaPlan
        fields = ('id', 'contract', 'current_month', 'document', 'description', 'created')


class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'contract', 'cash', 'pay_day')


class PaymentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'contract', 'cash', 'created', 'pay_day')


class SettingsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ('id', 'settings')


class SettingsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ('id', 'settings')


class DayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('id', 'created', 'day_date', 'moder', 'done', 'start_time', 'end_time')


class DayCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('id', 'day_date', 'moder', 'done', 'start_time', 'end_time')


class DiaryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = (
            'id', 'created', 'moder', 'cause', 'partner', 'other', 'result', 'destination_date', 'description',
            'process',
            'day')


class DiaryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = (
            'id', 'moder', 'cause', 'partner', 'other', 'result', 'destination_date', 'description',
            'process',
            'day')
