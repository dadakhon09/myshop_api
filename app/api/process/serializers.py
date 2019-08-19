from rest_framework.serializers import ModelSerializer

from app.api.users.serializers import UserSerializer
from app.model.process import Process
from app.api.negotiation.serializers import NegotiationListSerializer


class ProcessCreateSerializer(ModelSerializer):
    class Meta:
        model = Process
        fields = ('id', 'negotiation', 'cause', 'destination_date', 'description', 'status')


class ProcessListSerializer(ModelSerializer):
    negotiation = NegotiationListSerializer()
    moder = UserSerializer()

    class Meta:
        model = Process
        fields = ('id', 'moder', 'negotiation', 'cause', 'created', 'destination_date', 'description', 'status')


class ProcessUpdateSerializer(ModelSerializer):
    class Meta:
        model = Process
        fields = ('id', 'cause', 'destination_date', 'description', 'status')

