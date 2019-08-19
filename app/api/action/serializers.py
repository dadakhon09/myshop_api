from rest_framework.serializers import ModelSerializer

from app.model.action import Action
from app.api.partner.serializers import PartnerListSerializer
from app.api.users.serializers import UserSerializer


class ActionListSerializer(ModelSerializer):
    moder = UserSerializer()

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

