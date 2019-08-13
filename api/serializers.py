from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from api.models import Partner, Process, Payment, Action, Contract, Day, Diary, Negotiation, Tariff, MediaPlan, \
    Settings, UserProfile


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class UserProfileSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ('user', 'type')


class PartnerListSerializer(ModelSerializer):
    moder = UserSerializer()
    last_moder = UserSerializer()

    class Meta:
        model = Partner
        fields = (
            'id', 'ooo', 'contact_name', 'stationary_phone', 'mobile_phone', 'comment', 'address', 'created', 'moder',
            'last_moder', 'transfered', 'transfered_date')


class PartnerCreateSerializer(ModelSerializer):
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


# class PartnerTransferSerializer(ModelSerializer):
#     class Meta:
#         model = Partner
#         fields = (
#             'id', 'moder')
#
#     def update(self, instance, validated_data):
#         instance.last_moder = instance.moder
#         instance.moder = validated_data['moder']
#         return instance

class PartnerTransferSerializer(ModelSerializer):
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


class PartnerUpdateSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = (
            'id', 'ooo', 'contact_name', 'stationary_phone', 'mobile_phone', 'comment', 'address',
            'transfered', 'transfered_date')


class ActionListSerializer(ModelSerializer):
    subject = PartnerListSerializer()
    actor = UserSerializer()

    class Meta:
        model = Action
        fields = ('id', 'actor', 'action', 'subject', 'action_date', 'comment')


class ActionCreateSerializer(ModelSerializer):
    class Meta:
        model = Action
        fields = ('id', 'action', 'subject', 'comment')

    def create(self, validated_data):
        a = Action.objects.create(**validated_data)
        return a


class ActionUpdateSerializer(ModelSerializer):
    class Meta:
        model = Action
        fields = ('id', 'action', 'comment')


class TariffCreateSerializer(ModelSerializer):
    class Meta:
        model = Tariff
        fields = ('id', 'duration', 'name')


class TariffListSerializer(ModelSerializer):
    class Meta:
        model = Tariff
        fields = ('id', 'duration', 'name')


class ContractListSerializer(ModelSerializer):
    tariff = TariffListSerializer()

    class Meta:
        model = Contract
        fields = ('id', 'price', 'signing_date', 'activation_date', 'duration', 'tariff', 'tariff_price', 'description',
                  'created')


class ContractUpdateSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ('id', 'price', 'signing_date', 'activation_date', 'duration', 'tariff_price', 'description')


class ContractCreateSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ('id', 'price', 'signing_date', 'activation_date', 'duration', 'tariff', 'tariff_price', 'description')


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


class ProcessCreateSerializer(ModelSerializer):
    class Meta:
        model = Process
        fields = ('id', 'negotiation', 'cause', 'destination_date', 'description', 'status')


class ProcessListSerializer(ModelSerializer):
    negotiation = NegotiationListSerializer()

    class Meta:
        model = Process
        fields = ('id', 'negotiation', 'cause', 'created', 'destination_date', 'description', 'status')


class ProcessUpdateSerializer(ModelSerializer):
    class Meta:
        model = Process
        fields = ('id', 'cause', 'destination_date', 'description', 'status')


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


class PaymentCreateSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'contract', 'cash', 'pay_day')


class PaymentListSerializer(ModelSerializer):
    contract = ContractListSerializer()

    class Meta:
        model = Payment
        fields = ('id', 'contract', 'cash', 'created', 'pay_day')


class PaymentUpdateSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'cash', 'pay_day')


class SettingsCreateSerializer(ModelSerializer):
    class Meta:
        model = Settings
        fields = ('id', 'settings')


class SettingsListSerializer(ModelSerializer):
    class Meta:
        model = Settings
        fields = ('id', 'settings')


class DayListSerializer(ModelSerializer):
    moder = UserProfileSerializer()

    class Meta:
        model = Day
        fields = ('id', 'created', 'day_date', 'moder', 'done', 'start_time', 'end_time')


class DayUpdateSerializer(ModelSerializer):
    class Meta:
        model = Day
        fields = ('id', 'day_date', 'done', 'start_time', 'end_time')


class DayCreateSerializer(ModelSerializer):
    class Meta:
        model = Day
        fields = ('id', 'day_date', 'done', 'start_time', 'end_time')


class DiaryListSerializer(ModelSerializer):
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


class DiaryUpdateSerializer(ModelSerializer):
    class Meta:
        model = Diary
        fields = (
            'id', 'cause', 'other', 'result', 'destination_date', 'description')


class DiaryCreateSerializer(ModelSerializer):
    class Meta:
        model = Diary
        fields = (
            'id', 'cause', 'partner', 'other', 'result', 'destination_date', 'description',
            'process',
            'day')
