import datetime

from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response

from app.model import Action
from app.model.partner import Partner
from app.api.users.serializers import UserSerializer
from app.api.negotiation.serializers import NegotiationListSerializer


class PartnerListSerializer(ModelSerializer):
    moder = UserSerializer()
    last_moder = UserSerializer()
    negotiation_set = NegotiationListSerializer(many=True)

    class Meta:
        model = Partner
        fields = (
            'sphere', 'id', 'ooo', 'contact_name', 'stationary_phone', 'mobile_phone', 'comment', 'address', 'created',
            'moder', 'last_moder', 'transferred', 'transferred_date', 'negotiation_set')


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
        partners = list(request.data.getlist('partner_id'))
        user = User.objects.get(id=request.data.get('manager_id'))

        for partner in partners:
            p = Partner.objects.get(id=int(partner))

            if p.moder.id == user.id:
                return Response('You cant transfer to yourself')

            p.last_moder = p.moder
            p.moder = user
            p.transferred = True
            p.transferred_date = datetime.datetime.now()
            p.save()
            Action.objects.create(moder=user,
                                  action=f'partner {p} transferred to user {user}',
                                  subject=p)

        return Response(f'Transferred successfully to {user.username}', status=201)


class PartnerUpdateSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = ('id', 'ooo', 'contact_name', 'stationary_phone', 'mobile_phone', 'comment', 'address')
