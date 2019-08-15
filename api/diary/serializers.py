from rest_framework.serializers import ModelSerializer

from api.day.serializers import DayListSerializer
from api.models import Diary
from api.partner.serializers import PartnerListSerializer
from api.process.serializers import ProcessListSerializer
from api.users.serializers import UserSerializer


class DiaryListSerializer(ModelSerializer):
    moder = UserSerializer()
    partner = PartnerListSerializer()
    process = ProcessListSerializer()
    day = DayListSerializer()

    class Meta:
        model = Diary
        fields = (
            'id', 'created', 'moder', 'cause', 'partner', 'other', 'result', 'destination_date', 'description',
            'process', 'day')


class DiaryUpdateSerializer(ModelSerializer):
    class Meta:
        model = Diary
        fields = (
            'id', 'cause', 'other', 'result', 'destination_date', 'description')


class DiaryCreateSerializer(ModelSerializer):
    class Meta:
        model = Diary
        fields = (
            'id', 'cause', 'partner', 'other', 'result', 'destination_date', 'description', 'process', 'day')
