from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Partner, Process, Payment, Action, Contract, Day, Diary, Negotiation, Tariff, MediaPlan, \
    Settings, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ('user', 'type')


class PartnerListSerializer(serializers.ModelSerializer):
    moder = UserSerializer()
    last_moder = UserSerializer()

    class Meta:
        model = Partner
        fields = (
            'id', 'ooo', 'contact_name', 'stationary_phone', 'mobile_phone', 'comment', 'address', 'created', 'moder',
            'last_moder', 'transfered', 'transfered_date')


class PartnerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = (
            'id', 'ooo', 'contact_name', 'stationary_phone', 'mobile_phone', 'comment', 'address',
            'transfered', 'transfered_date')

    # def create(self, validated_data):
    #     p = Partner.objects.create(**validated_data)
    #     p.moder = self.context['request'].user
    #     p.save()
    #     print(self.context['request'])
    #     return p


# class PartnerTransferSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Partner
#         fields = (
#             'id', 'moder')
#
#     def update(self, instance, validated_data):
#         instance.last_moder = instance.moder
#         instance.moder = validated_data['moder']
#         return instance

class PartnerTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ()

    def create(self, validated_data):
        request = self.context['request']
        partners = request.data.getlist('partner')
        for partner in partners:
            p = Partner.objects.get(id=int(partner))
            p.last_moder = p.moder
            p.moder = User.objects.get(id=request.data.get('user_id'))
            p.save()

        return request


class PartnerUpdateSerializer(serializers.ModelSerializer):
    # moder = UserProfileSerializer()

    class Meta:
        model = Partner
        fields = (
            'id', 'ooo', 'contact_name', 'stationary_phone', 'mobile_phone', 'comment', 'address',
            'transfered', 'transfered_date')


class ActionListSerializer(serializers.ModelSerializer):
    subject = PartnerListSerializer()
    actor = UserSerializer()

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


class TariffCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = ('id', 'duration', 'name')


class TariffListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = ('id', 'duration', 'name')


class ContractListSerializer(serializers.ModelSerializer):
    tariff = TariffListSerializer()

    class Meta:
        model = Contract
        fields = ('id', 'price', 'signing_date', 'activation_date', 'duration', 'tariff', 'tariff_price', 'description',
                  'created')


class ContractCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('id', 'price', 'signing_date', 'activation_date', 'duration', 'tariff', 'tariff_price', 'description')


class NegotiationListSerializer(serializers.ModelSerializer):
    contract = ContractListSerializer()
    partner = PartnerListSerializer()

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
    negotiation = NegotiationListSerializer()

    class Meta:
        model = Process
        fields = ('id', 'negotiation', 'cause', 'created', 'destination_date', 'description', 'status')


class MediaPlanCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaPlan
        fields = ('id', 'contract', 'current_month', 'document', 'description')


class MediaPlanListSerializer(serializers.ModelSerializer):
    contract = ContractListSerializer()

    class Meta:
        model = MediaPlan
        fields = ('id', 'contract', 'current_month', 'document', 'description', 'created')


class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'contract', 'cash', 'pay_day')


class PaymentListSerializer(serializers.ModelSerializer):
    contract = ContractListSerializer()

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
    moder = UserProfileSerializer()

    class Meta:
        model = Day
        fields = ('id', 'created', 'day_date', 'moder', 'done', 'start_time', 'end_time')


class DayCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('id', 'day_date', 'moder', 'done', 'start_time', 'end_time')


class DiaryListSerializer(serializers.ModelSerializer):
    moder = UserSerializer()
    partner = PartnerListSerializer()
    process = ProcessListSerializer()
    day = DayListSerializer()

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
