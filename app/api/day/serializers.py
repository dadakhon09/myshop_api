from rest_framework.serializers import ModelSerializer

from app.model.day import Day
from app.api.users.serializers import UserSerializer


class DayListSerializer(ModelSerializer):
    moder = UserSerializer()

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


class DayStartSerializer(ModelSerializer):
    class Meta:
        model = Day
        fields = ('id', 'day_date', 'start_time')


class DayEndSerializer(ModelSerializer):
    class Meta:
        model = Day
        fields = ('id', 'day_date', 'done', 'end_time')
