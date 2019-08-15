from rest_framework.serializers import ModelSerializer

from api.models import Action
from api.partner.serializers import PartnerListSerializer
from api.users.serializers import UserSerializer


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

