import datetime

from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from app.model import Action
from app.model.partner import Partner
from app.api.users.serializers import UserSerializer


class PartnerListSerializer(ModelSerializer):
    moder = UserSerializer()
    last_moder = UserSerializer()

    class Meta:
        model = Partner
        fields = (
            'id', 'ooo', 'contact_name', 'stationary_phone', 'mobile_phone', 'comment', 'address', 'created', 'moder',
            'last_moder', 'transferred', 'transferred_date')


class PartnerCreateSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = (
            'id', 'ooo', 'contact_name', 'stationary_phone', 'mobile_phone', 'comment', 'address')


class PartnerTransferSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = ()

    def create(self, validated_data):
        request = self.context['request']
        partners = request.data.getlist('partner_id')
        user = User.objects.get(id=request.data.get('user_id'))
        for partner in partners:
            p = Partner.objects.get(id=int(partner))
            if p.moder.id == user.id:
                continue
            p.last_moder = p.moder
            p.moder = user
            p.transferred = True
            p.transferred_date = datetime.datetime.now()
            p.save()
            Action.objects.create(moder=user,
                                  action=f'partner {p} transferred to user {user}',
                                  subject=p)
        return request




class PartnerUpdateSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = ('id', 'ooo', 'contact_name', 'stationary_phone', 'mobile_phone', 'comment', 'address')
