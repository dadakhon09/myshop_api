from rest_framework.serializers import ModelSerializer

from app.api.day.serializers import DayListSerializer
from app.model.dairy import Diary
from app.api.partner.serializers import PartnerListSerializer
from app.api.process.serializers import ProcessListSerializer
from app.api.users.serializers import UserSerializer


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
