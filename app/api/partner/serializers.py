from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from app.model.action import Action
from app.model.partner import Partner
from app.api.users.serializers import UserSerializer


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
            'id', 'ooo', 'contact_name', 'stationary_phone', 'mobile_phone', 'comment', 'address', 'transfered',
            'transfered_date')


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
            'id', 'ooo', 'contact_name', 'stationary_phone', 'mobile_phone', 'comment', 'address', 'transfered',
            'transfered_date')
